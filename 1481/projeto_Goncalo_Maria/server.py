import socket
import threading
from security import detect_personal_data
from datetime import datetime
from profiles import add_profile
from profiles import load_profiles
from profiles import find_profile

HOST = "127.0.0.1"
PORT = 5000

clients = {}

def get_time():
    return datetime.now().strftime("%H:%M")

def broadcast(message):

    for client in clients.values():
        try:
            client.send(message.encode())
        except:
            pass

def handle_client(client):

    client.send("[SERVER] Use /login ou /register".encode())

    name = None

    # ---------------- AUTHENTICATION ----------------
    while not name:

        message = client.recv(1024).decode()

        # REGISTER
        if message == "/register":

            client.send("Username: ".encode())
            username = client.recv(1024).decode()

            client.send("Password: ".encode())
            password = client.recv(1024).decode()

            client.send("Age: ".encode())
            age = client.recv(1024).decode()

            client.send("Gender: ".encode())
            gender = client.recv(1024).decode()

            if find_profile(username):
                client.send("[SERVER] Username já existe.".encode())
                continue

            profile = {
                "username": username,
                "password": password,
                "age": age,
                "gender": gender
            }

            add_profile(profile)

            client.send("[SERVER] Registo criado. Faça login.".encode())


        # LOGIN
        elif message == "/login":

            client.send("Username: ".encode())
            username = client.recv(1024).decode()

            client.send("Password: ".encode())
            password = client.recv(1024).decode()

            profile = find_profile(username)

            if profile and profile["password"] == password:

                if username in clients:
                    client.send("[SERVER] Utilizador já está online.".encode())
                    continue

                name = username
                clients[name] = client

                client.send("[SERVER] Login bem sucedido.".encode())

            else:
                client.send("[SERVER] Login inválido.".encode())

        else:
            client.send("[SERVER] Use /login ou /register".encode())


    # ---------------- USER CONNECTED ----------------
    print(f"\n[{get_time()}] [SERVER]: {name} conectou-se.")
    broadcast(f"\n[{get_time()}] [SERVER] {name} entrou no chat\n")


    # ---------------- CHAT LOOP ----------------
    while True:

        try:
            message = client.recv(1024).decode()

            if not message:
                break


            # EXIT
            if message.lower() == "/exit":
                break


            # USERS
            if message == "/users":

                user_list = ", ".join(clients.keys())

                client.send(
                    f"[{get_time()}] [SERVER] Utilizadores online: {user_list}".encode()
                )
                continue


            # PROFILES
            if message == "/profiles":

                profiles = load_profiles()

                text = "\nPerfis disponíveis:\n"

                for p in profiles:
                    text += f"{p['username']} | {p['age']} | {p['gender']}\n"

                client.send(text.encode())
                continue


            # PRIVATE MESSAGE
            if message.startswith("/msg"):

                try:
                    _, target, private_msg = message.split(" ", 2)
                except ValueError:
                    client.send("[SERVER] Uso: /msg utilizador mensagem".encode())
                    continue

                if target not in clients:
                    client.send(
                        f"[{get_time()}] [SERVER] Utilizador não encontrado.".encode()
                    )
                    continue

                clients[target].send(
                    f"[{get_time()}] [PM] {name}: {private_msg}".encode()
                )

                client.send(
                    f"[{get_time()}] [PM → {target}] {private_msg}".encode()
                )

                continue


            # GDPR CHECK
            warning = detect_personal_data(message)

            if warning:

                action, data_type = warning

                if action == "block":
                    client.send(
                        f"Mensagem bloqueada por conter conteúdo pessoal ({data_type})".encode()
                    )
                    continue

                if action == "warn":

                    client.send(
                        f"Aviso: possível {data_type} na mensagem. Enviar mesmo assim? (s/n)".encode()
                    )

                    confirm = client.recv(1024).decode()

                    if confirm.lower() != "s":
                        client.send("Mensagem bloqueada.".encode())
                        continue


            print(f"\n[{get_time()}] {name}: {message}")

            broadcast(f"[{get_time()}] {name}: {message}")


        except:
            break


    # ---------------- DISCONNECT ----------------
    del clients[name]

    print(f"\n[{get_time()}] [SERVER]: {name} desconectou-se.")

    broadcast(f"\n[{get_time()}] [SERVER] {name} saiu do chat\n")

    client.close()


def start_server():

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen()

    print(f"[{get_time()}] Servidor iniciado...")

    while True:

        client, addr = server.accept()

        print(f"[{get_time()}] Novo cliente conectado:", addr)

        thread = threading.Thread(
            target=handle_client,
            args=(client,)
        )

        thread.start()


start_server()
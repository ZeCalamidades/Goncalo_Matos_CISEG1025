import socket
import threading
from security import detect_personal_data
from datetime import datetime

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

    name = client.recv(1024).decode()
    clients[name] = client

    print(f"\n[{get_time()}] [SERVER]: {name} conectou-se.")

    broadcast(f"\n[{get_time()}] [SERVER] {name} entrou no chat\n")

    while True:

        try:
            message = client.recv(1024).decode()

            if not message:
                break
            
            
            # comando /exit
            if message.lower() == "/exit":
                break
            
            # comando /users    
            if message == "/users":

                user_list = ", ".join(clients.keys())

                client.send(
                    f"[{get_time()}] [SERVER] Utilizadores online: {user_list}".encode())

                continue
            #comando /msg
            if message.startswith("/msg"):

                try:
                        _, target, private_msg = message.split(" ", 2)
                except ValueError:
                    client.send("[SERVER] Uso: /msg utilizador mensagem".encode())
                    continue

                if target not in clients:
                    client.send(f"[{get_time()}] [SERVER] Utilizador não encontrado.".encode())
                    continue

                clients[target].send(
                    f"[{get_time()}] [PM] {name}: {private_msg}".encode())

                client.send(
                    f"[{get_time()}] [PM → {target}] {private_msg}".encode())

                continue
            print(f"\n[{get_time()}] {name}: {message}")

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

            broadcast(f"[{get_time()}] {name}: {message}")

        except:
            break

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
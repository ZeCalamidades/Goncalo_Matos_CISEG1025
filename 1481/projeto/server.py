import socket
import threading
from security import detect_personal_data
from datetime import datetime

#HOST = "0.0.0.0"
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

    print(f"[SERVER]: {name} conectou-se.")

    broadcast(f"\n[{get_time()}] [SERVER] {name} entrou no chat\n")

    while True:

        try:
            message = client.recv(1024).decode()

            if not message:
                break

            print(f"{name}: {message}")

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

    print(f"[SERVER]: {name} desconectou-se.")

    broadcast(f"\n[{get_time()}] [SERVER] {name} saiu do chat\n")

    del clients[name]
    client.close()


def start_server():

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen()

    print("Servidor iniciado...")

    while True:

        client, addr = server.accept()

        print("Novo cliente conectado:", addr)

        thread = threading.Thread(
            target=handle_client,
            args=(client,)
        )

        thread.start()


start_server()
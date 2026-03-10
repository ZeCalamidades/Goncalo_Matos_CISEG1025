import socket
import threading

HOST = "0.0.0.0"    #online
#HOST = "127.0.0.1"   #host
PORT = 5000

clients = []

def handle_client(client):

    while True:
        try:
            message = client.recv(1024).decode()
            print(message)

            broadcast(message)

        except:
            clients.remove(client)
            client.close()
            break


def broadcast(message):

    for client in clients:
        try:
            client.send(message.encode())
        except:
            pass


def start_server():

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen()

    print("Servidor iniciado...")

    while True:

        client, addr = server.accept()
        print("Novo cliente conectado:", addr)

        clients.append(client)

        thread = threading.Thread(target=handle_client, args=(client,))
        thread.start()


start_server()
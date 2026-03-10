import socket
import threading

#HOST = "192.168.68.100" #host
HOST = "127.0.0.1"     #online
PORT = 5000

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))


def receive():

    while True:
        try:
            message = client.recv(1024).decode()
            print(message)
        except:
            break


def send():

    while True:
        message = input("")
        client.send(message.encode())


threading.Thread(target=receive).start()
send()
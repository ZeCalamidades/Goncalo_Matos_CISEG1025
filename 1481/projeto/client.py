import socket
import threading
from datetime import datetime


#HOST = "192.168.68.100" #online
HOST = "127.0.0.1"     #host
PORT = 5000

name = "" 


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))


def get_time():
    return datetime.now().strftime("%H:%M")

def receive():

    while True:
        try:
            message = client.recv(1024).decode()

            if not message:
                break

            print(message)

        except:
            break
def send():

    while True:
        message = input("> ")
        client.send(message.encode())

def login():
    global name
    name = input("Nome: ")
    client.send(name.encode())


login()

threading.Thread(target=receive).start()

send()
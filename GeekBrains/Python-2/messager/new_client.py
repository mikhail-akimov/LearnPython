import socket
from select import select
import sys

address = ('localhost', 7777)

def echo_client():
    with socket.create_connection(address) as sock:
        while True:
            data = sock.recv(1024).decode('utf-8')
            if data:
                print('Response :', data)
            msg = input('Your message:')
                if msg == 'exit':
                    break
                sock.sendall(msg.encode('utf-8'))

if __name__ == '__main__':
    echo_client()
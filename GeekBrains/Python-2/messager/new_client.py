import socket
import sys
from time import time
import json


class Client:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.sock = None

    def connect(self):
        try:
            self.sock = socket.create_connection((self.host, self.port))
        except ConnectionRefusedError as ex:
            print(ex)
            sys.exit(1)
        except KeyboardInterrupt:
            self.sock.close()
            sys.exit(1)

    def send_message(self, message):
        self.sock.sendall(json.dumps(message).encode('utf-8'))
        self.recive_response()

    def recive_response(self):
        data = json.loads(self.sock.recv(1024).decode('utf-8'))
        print(data)

    def presense(self):
        message = {
            "action": "presence",
            "time": int(time()),
            "type": "status",
            "user": {
                "account_name": 'test_user',
                "status": "i`m here!"
            }
        }

        return message


def client_start():
    if len(sys.argv) == 1:
        print('Enter host name and port')
        sys.exit(1)
    elif len(sys.argv[1]) < 7:
        print('Incorrect server-address')
        sys.exit(1)
    else:
        host = sys.argv[1]

        if len(sys.argv) < 3:
            port = str(7777)
        else:
            port = sys.argv[2]

        return host, port


client = Client(client_start()[0], client_start()[1])
client.connect()
client.send_message(client.presense())


import socket
import sys
from time import time
import json
import argparse


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

    def receive_response(self):
        data = self.sock.recv(1024).decode('utf-8')
        return data

    def auth(self, login, password):
        message = {
            "action": "authenticate",
            "time": int(time()),
            "user": {
                "account_name": login,
                "password": password
            }
        }
        return message

    def presence(self):
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

    def message(self, text):
        message = {
            "action": "msg",
            "time": int(time()),
            "to": '#room_name',
            "from": 'account_name',
            'message': str(text)
        }
        return message


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Client app')
    parser.add_argument('address', help='Server host', default='localhost')
    parser.add_argument('port', help='Server port', type=int, default=7777)
    parser.add_argument('mode', help='Read/write mode', type=str)
    args = parser.parse_args()

    print(args)

    client = Client(args.address, args.port)
    client.connect()
    client.send_message(client.presence())
    while True:
        if args.mode == 'r':
            try:
                while True:
                    data = client.receive_response()
                    if data:
                        print('Response :', data)
            except KeyboardInterrupt:
                client.sock.close()
                sys.exit(0)
        elif args.mode == 'w':
            try:
                msg = input('Your message:')

                if msg == 'exit':
                    break
                client.send_message(client.message(msg))
            except KeyboardInterrupt:
                client.sock.close()
                sys.exit(0)
        else:
            print('Impossible scenario')

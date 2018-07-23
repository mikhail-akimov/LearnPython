import socket
import json
import sys
from time import time

if len(sys.argv) == 1:
    print('Please enter host address...')
    sys.exit(1)
elif len(sys.argv) == 2:
    port = 7777
else:
    port = sys.argv[2]

host = sys.argv[1]


def presence():
    message = {
        "action": "presence",
        "time": int(time()),
        "type": "status",
        "user": {
            "account_name": 'test_user',
            "status": "i`m here!"
        }
    }
    return json.dumps(message)


def auth():
    message = {
        "action": "authenticate",
        "time": int(time()),
        "user": {
            "account_name": "user",
            "password": "password"
        }
    }
    return json.dumps(message)

try:
    with socket.create_connection((host, port)) as sock:
        sock.sendall(presence().encode("utf-8"))
        data = json.loads(sock.recv(1024).decode("utf-8"))
        print(data['response'])


except ConnectionRefusedError as ex:
    print(ex)


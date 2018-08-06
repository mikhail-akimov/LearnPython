import socket
from time import time
import json
import argparse


def get_user(name, status):
    return {
        "account_name": name,
        "status": status
    }


def get_presence_message(user):
    return {

        "action": "presence",
        "time": time(),
        "type": "status",
        "user": user

    }


def format_message(dict_message):
    return json.dumps(dict_message).encode("utf-8")


def mainloop(address, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((address, port))

    while True:
        command = int(input("Input 1 or 2: "))

        if command == 1:
            user = input("Input username: ")
            status = input("Input status: ")

            s.send(format_message(get_presence_message(get_user(user, status))))
            data = s.recv(1024)
            if data:
                print(data.decode("utf-8"))
        elif command == 2:
            s.close()
            break
        else:
            print("Wrong command!")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Client app')
    parser.add_argument('address', help='Server host', default="localhost")
    parser.add_argument('port', help='Server port', type=int, default=7777)

    args = parser.parse_args()

    mainloop(args.address, args.port)

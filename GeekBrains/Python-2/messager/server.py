import socket
import json
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-a", help="Enter address to listen")
parser.add_argument("-p", help="Enter port to listen")
args = parser.parse_args()

if not args.a:
    host = ""
else:
    host = args.a

if not args.p:
    port = int(7777)
else:
    port = int(args.p)

print(host, port)


with socket.socket() as sock:
    sock.bind((host, port))
    sock.listen()

    while True:
        conn, addr = sock.accept()

        with conn:
            while True:
                data = json.loads(conn.recv(1024).decode("utf-8"))
                if not data:
                    break

                print(data)

                if data["action"] == "presence":
                    response = {
                        "response": 200
                    }
                    response = json.dumps(response).encode("utf-8")
                    conn.sendall(response)
                else:
                    response = {
                        "response": 300
                    }
                    response = json.dumps(response).encode("utf-8")
                    conn.sendall(response)

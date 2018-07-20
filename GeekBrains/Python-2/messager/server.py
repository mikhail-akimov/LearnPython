import socket
import json

with socket.socket() as sock:
    sock.bind(("", 7777))
    sock.listen()

    while True:
        conn, addr = sock.accept()

        with conn:
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

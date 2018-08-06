import socket
import json
import argparse
import select
import time

parser = argparse.ArgumentParser(description='Server side')
parser.add_argument("-a", help="Enter address to listen", default='')
parser.add_argument("-p", help="Enter port to listen", type=int, default=7777)
args = parser.parse_args()


def presence_response():
    response = {
        "response": 200}
    response = json.dumps(response).encode("utf-8")
    return response

with socket.socket() as sock:
    sock.bind((args.a, args.p))
    sock.listen()
    sock.settimeout(0.2)
    clients = []

    while True:
        try:
            conn, addr = sock.accept()
        except OSError as e:
            pass
        else:
            print('Получен запрос на подключение от {}'.format(addr))
            clients.append(conn)
        finally:
            w = []
            r = []

            try:
                r, w, e = select.select(clients, clients, [], 0)
            except Exception as e:
                pass
            for client in clients:
                try:
                    if client in r:
                        msg = json.loads(client.recv(1024).decode('utf-8'))
                        if msg['action'] == "presence":
                            client.sendall(presence_response())
                        elif msg['action'] == 'msg':
                            print('Recived {} from {}'.format(msg, client.getpeername()))

                            for client_r in clients:
                                client_r.sendall(json.dumps(msg['message']).encode('utf-8'))
                                print('Sended {} to {}'.format(msg['message'], client_r.getpeername()))
                        else:
                            break
                except:
                    clients.remove(client)
                    print('{} удалён'.format(client))



                    # with conn:
                    #     data = json.loads(conn.recv(1024).decode("utf-8"))
                    #     if not data:
                    #         break
                    #     print(data)
                    #     if data["action"] == "presence":
                    #         response = {
                    #             "response": 200
                    #         }
                    #         response = json.dumps(response).encode("utf-8")
                    #         conn.sendall(response)
                    #     else:
                    #         response = {
                    #             "response": 300
                    #         }
                    #         response = json.dumps(response).encode("utf-8")
                    #         conn.sendall(response)
#



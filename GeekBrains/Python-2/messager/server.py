import socket
import json
import argparse
import select
import time
import utils

parser = argparse.ArgumentParser(description='Server side')
parser.add_argument("-a", help="Enter address to listen", default='')
parser.add_argument("-p", help="Enter port to listen", type=int, default=7777)
args = parser.parse_args()


@utils.log("Receiving messages")
def receive(sender):
    message = json.loads(sender.recv(1024).decode('utf-8'))
    return message


@utils.log("Sending message")
def send(message, receiver):
    receiver.sendall(json.dumps(message).encode('utf-8'))


def presence_response():
    response = {
        "response": 200}
    response = json.dumps(response).encode("utf-8")
    return response


with socket.socket() as sock:
    sock.bind((args.a, args.p))
    sock.listen(5)
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
            for client in w:
                try:
                    if client in r:
                        msg = receive(client)
                        print(msg)
                        if msg:
                            if msg['action'] == "presence":
                                client.sendall(presence_response())
                            elif msg['action'] == 'msg':
                                print('received {} from {}'.format(msg, client.getpeername()))

                                for client_r in clients:
                                    send(msg['message'], client_r)
                                    print('Sended {} to {}'.format(msg['message'], client_r.getpeername()))
                            else:
                                break
                except OSError as e:
                    print('Error!')
                    print(e)
                    clients.remove(client)
                    print('{} удалён'.format(client))

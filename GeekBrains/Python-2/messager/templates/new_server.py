import socket
import json
import argparse
import select
import time

parser = argparse.ArgumentParser(description='Server side')
parser.add_argument("-a", help="Enter address to listen", default='')
parser.add_argument("-p", help="Enter port to listen", type=int, default=7778)
args = parser.parse_args()


def read_requests(clients):
    responses = {}

    for sock in clients:
        try:
            data = sock.recv(1024).decode('utf-8')
            responses[sock] = data

        except:
            print('Клиент {} {} отключился'.format(sock.fileno(), sock.getpeername()))
            clients.remove(sock)
        return responses


def write_responses(requests, clients):
    for sock in clients:
        if sock in requests:
            try:
                resp = requests[sock].encode('utf-8')
                print(resp)
                test_len = sock.send(resp.upper())
            except:
                print('Клиент {} отключился'.format(sock.getpeername()))
                sock.close()
                clients.remove(sock)


def main_loop():
    clients = []
    s = socket.socket()
    s.bind((args.a, args.p))
    s.listen(5)
    s.settimeout(0.2)

    while True:
        try:
            conn, addr = s.accept()
        except OSError as e:
            pass
        else:
            print('Получен запрос на соединение с {}'.format(addr))
            clients.append(conn)
        finally:
            wait = 0
            r = []
            w = []
            try:
                r, w, e = select.select(clients, clients, [], wait)
            except:
                pass

            requests = read_requests(r)
            if requests:
                write_responses(requests, w)


main_loop()
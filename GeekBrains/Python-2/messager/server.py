import socket
import json
import argparse
import select
import time

parser = argparse.ArgumentParser(description='Server side')
parser.add_argument("-a", help="Enter address to listen", default='')
parser.add_argument("-p", help="Enter port to listen", type=int, default=7777)
args = parser.parse_args()


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

            try:
                r, w, e = select.select([], clients, [], 0)
            except Exception as e:
                pass

            for s_client in w:
                print('here')
                timestr = time.ctime(time.time()) + '\n'
                try:
                    s_client.send(timestr.encode('utf-8'))
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
                except:
                    clients.remove(s_client)
                    print('{} удалён'.format(s_client))


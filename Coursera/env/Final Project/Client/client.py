import socket
import time


class ClientError(socket.error):
    pass


class Client:
    def __init__(self, host, port, timeout=None):
        self.host = host
        self.port = port
        self.timeout = timeout

    def _connect(self):
        return socket.create_connection((self.host, self.port), self.timeout)

    def put(self, metric_name, metric_value, timestamp=time.time()):
        try:
            with self._connect() as sock:
                message = ("put {} {} {}\n".format(metric_name, metric_value, str(int(timestamp))))
                try:
                    sock.sendall(message.encode("utf8"))
                    data = sock.recv(1024)

                    # if data.decode('utf8') != 'ok\n':
                    #     raise ClientError(Exception)
                except socket.error:
                    raise ClientError

        except ConnectionRefusedError:
            print('Connection Refused')

        except ConnectionResetError:
            print('Connection Aborted')

    def get(self, metric_name=None):
        message = ("get {}\n".format(metric_name))
        try:
            with self._connect() as sock:
                sock.sendall(message.encode("utf8"))
                data = sock.recv(1024)
                print(data.decode('utf8'))

        except socket.error:
            raise ClientError

client = Client("127.0.0.1", 10001, timeout=15)
# client.put("CONTUR.cpu", 1111)
client.get('CONTUR.cpu')
































# class ClientError(Exception):
#     pass
#
#
# class Client:
#     def __init__(self, host, port, timeout=None):
#         self.host = host
#         self.port = port
#         self.timeout = timeout
#         self.sock = None
#
#     def __connect(self):
#         self.sock = socket.create_connection((self.host, self.port), self.timeout)
#
#     def put(self, metric_name, metric_value, timestamp=time.time()):
#         metric_name = metric_name
#         metric_value = float(metric_value)
#         timestamp = int(timestamp)
#
#         # try:
#         self.__connect()
#         print(type(self.sock))
#         # self.sock.sendall("put {metric_name} {metric_value} {timestamp}".format(metric_name, metric_value, timestamp))
#         print("The {} value was {} at {}".format(metric_name, metric_value, timestamp))
#         # except:
#         #     print(ClientError)
#
#     @staticmethod
#     def get(self):
#         pass
#
# client = Client("127.0.0.1", 10001, timeout=15)
# client.put("CONTUR.cpu", 1111)
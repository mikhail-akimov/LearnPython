from chat import Chat
import asyncio
import select


class ChatServer(Chat):

    def __init__(self, config):
        super().__init__(config)
        self._setup(config)
        self.client = None
        self.address = None
        self.connect()
        self.clients = []

    def _setup(self, config):
        self.timeout = config["timeout"]
        self.listen = config["listen"]

    def send_message(self, msg):
        if self.client is not None:
            self.client.sendall(msg)

    def receive_message(self):
        return self.s.recv(1024)

    def connect(self):
        self.s.bind((self.host, self.port))
        self.s.listen(self.listen)
        # self.s.settimeout(self.timeout)

    def start_chat(self):
        raise NotImplementedError

    def main_loop(self):
        while True:
            print('Cycling...')
            try:
                conn, addr = self.s.accept()
            except OSError as e:
                print(e)
            else:
                print('Получен запрос на подключение от {}'.format(addr))
                self.clients.append(conn)

            finally:
                w = []
                r = []

                try:
                    r, w, e = select.select(self.clients, self.clients, [], 0)

                except Exception as e:
                    print(e)

                print('W-list is {}'.format(w))
                print('R-list is {}'.format(r))
                for client in self.clients:
                    try:
                        client.send(b'Hello world!')
                    except OSError as e:
                        print('Error!')
                        print(e)
                        self.clients.remove(client)
                        print('{} удалён'.format(client))

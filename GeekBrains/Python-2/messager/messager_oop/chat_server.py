from chat import Chat
import select
from jim import convert_from_bytes


class ChatServer(Chat):

    def __init__(self, config):
        super().__init__(config)
        self._setup(config)
        self.client = None
        self.address = None
        self.connect()
        self.new_clients = []
        self.clients = dict()

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
        self.s.settimeout(self.timeout)

    def start_chat(self):
        raise NotImplementedError

    def main_loop(self):
        while True:
            try:

                conn, addr = self.s.accept()

            except OSError as e:
                pass
            else:
                print('Получен запрос на подключение от {}'.format(addr))
                self.new_clients.append(conn)
            finally:
                r = []
                w = []
                e = []
                try:
                    r, w, e = select.select(self.new_clients, self.new_clients, [], 0)

                except Exception as ex:
                    pass

                for client in r:
                    try:
                        data = convert_from_bytes(client.recv(1024))
                        print('W-list contains {}'.format(w))
                        print('R-list contains {}'.format(r))
                        if data:
                            if str(data["action"]) == 'presence':
                                self.clients = {data['user']: client}
                            elif str(data["action"]) == 'msg':
                                # print(self.clients[data['to']])
                                print(data)
                            else:
                                print('Oooops')
                            print(data)
                    except OSError as e:
                        print('Error!')
                        print(e)
                        self.new_clients.remove(client)
                        print('{} удалён'.format(client))

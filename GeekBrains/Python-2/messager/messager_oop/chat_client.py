from chat import Chat
import sys
from jim import JimMessage, JimAuthenticate, JimMsg, JimPresence, JimProbe, JimJoin, Jim, convert_to_bytes
import json


class ChatClient(Chat):

    def __init__(self, config):
        super().__init__(config)
        self._setup(config)
        self.connect()

    def send_message(self, msg):
        self.s.sendall(msg)

    def receive_message(self):
        return json.loads(self.s.recv(1024))

    def connect(self):
        self.s.connect((self.host, self.port))

    def start_chat(self):
        raise NotImplementedError

    def add_contact(self, contact):
        db.ContactList(self, contact)

    def main_loop(self):
        mode = 'w'

        login = input('Enter your name: ')

        while True:
            if mode == 'r':
                try:
                    while True:
                        data = self.receive_message()
                        if data:
                            print('Response :', data)
                except KeyboardInterrupt:
                    self.s.close()
                    sys.exit(0)
            elif mode == 'w':
                try:
                    msg = input('Your message: ')

                    if msg == 'exit':
                        break
                    elif msg == 'presence':
                        self.send_message(convert_to_bytes(JimPresence(login, "Online")))
                    elif msg == 'msg':

                        to = input('For who: ')
                        txt = input('Enter your message')

                        self.send_message(convert_to_bytes(JimMsg()))
                    else:
                        self.send_message(convert_to_bytes(msg))
                except KeyboardInterrupt:
                    self.s.close()
                    sys.exit(0)
            else:
                print('Impossible scenario')



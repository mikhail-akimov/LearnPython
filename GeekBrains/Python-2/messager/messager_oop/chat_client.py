from chat import Chat


class ChatClient(Chat):

    def __init__(self, config):
        super().__init__(config)
        self._setup(config)
        self.connect()

    def send_message(self, msg):
        self.s.sendall(msg)

    def receive_message(self):
        return self.s.recv(1024)

    def connect(self):
        self.s.connect((self.host, self.port))
        print(self.s)

    def start_chat(self):
        raise NotImplementedError

    def add_contact(self, contact):
        db.ContactList(self, contact)


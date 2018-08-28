from chat import Chat
import storage


class ChatClient(Chat):

    def __init__(self, config):
        super().__init__(config)
        self._setup(config)

    def receive_message(self):
        raise NotImplementedError

    def connect(self):
        self.s.connect((self.host, self.port))

    def start_chat(self):
        raise NotImplementedError

    def add_contact(self, contact):
        db.ContactList(self, contact)


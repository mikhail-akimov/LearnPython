from chat import Chat


class ChatServer(Chat):

    def __init__(self, config):
        super().__init__(config)
        self._setup(config)

    def _setup(self, config):
        self.timeout = config["timeout"]
        self.listen = config["listen"]

    def receive_message(self):
        raise NotImplementedError

    def connect(self):
        self.s.bind((self.host, self.port))
        self.s.listen(self.listen)
        self.s.settimeout(self.timeout)
        self.s.accept()

    def start_chat(self):
        raise NotImplementedError
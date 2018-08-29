import socket


class Chat:
    host = None
    port = None

    def __init__(self, config):
        self.host = config["host"]
        self.port = config["port"]
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def _setup(self, config):
        pass

    def send_message(self, msg):
        raise NotImplementedError

    def receive_message(self):
        raise NotImplementedError

    def connect(self):
        raise NotImplementedError

    def start_chat(self):
        raise NotImplementedError


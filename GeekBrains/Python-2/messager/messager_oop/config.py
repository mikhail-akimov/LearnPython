class Config:
    host = None
    port = None
    listen = None
    timeout = None

    def __init__(self, method):
        self.host, self.port, self.listen, self.timeout = method.load()

    def get_dict_config(self):
        return {"host": self.host,
                "port": self.port,
                "listen": self.listen,
                "timeout": self.timeout
                }


class LoadFromFile:

    def __init__(self, filename):
        self.filename = filename

    def load(self):
        pass


class LoadFromConsole:

    def load(self):
        host = input("Input host: ")
        port = int(input("Input port: "))
        listen = int(input("Input listen: "))
        timeout = int(input("Input timeout: "))

        return host, port, listen, timeout


class LoadFromArgparse:
    pass


class LoadFromParams:
    def load(self):
        host = 'localhost'
        port = 7777
        listen = 10
        timeout = 0.2

        return host, port, listen, timeout

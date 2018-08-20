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
        port = input("Input port: ")
        listen = input("Input listen: ")
        timeout = input("Input timeout: ")

        return (host, port, listen, timeout)


class LoadFromArgparse:
    pass


from chat_server import ChatServer
from config import Config, LoadFromArgparse, LoadFromConsole, LoadFromFile, LoadFromParams
import select


if __name__ == '__main__':

    config = Config(LoadFromParams())

    server = ChatServer(config.get_dict_config())

    server.main_loop()
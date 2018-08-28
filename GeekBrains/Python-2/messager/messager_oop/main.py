from chat_client import ChatClient
from chat_server import ChatServer
from config import Config, LoadFromArgparse, LoadFromConsole, LoadFromFile


if __name__ == '__main__':

    config = Config(LoadFromFile())

    server = ChatServer(LoadFromConsole)
    client = ChatClient(LoadFromConsole)


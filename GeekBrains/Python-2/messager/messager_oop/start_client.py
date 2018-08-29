from chat_client import ChatClient
from config import Config, LoadFromArgparse, LoadFromConsole, LoadFromFile, LoadFromParams


if __name__ == '__main__':

    config = Config(LoadFromParams())

    client = ChatClient(config.get_dict_config())

    while True:
        print('Waiting...')
        print(client.receive_message())

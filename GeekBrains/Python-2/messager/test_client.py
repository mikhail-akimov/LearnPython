import pytest
import sys
import new_client
from time import time


def test_auth_msg():
    msg = new_client.Client.auth('self', 'login', 'password')

    assert msg == {
            "action": "authenticate",
            "time": int(time()),
            "user": {
                "account_name": 'login',
                "password": 'password'
            }
        }


def test_presence_msg():
    msg = new_client.Client.presence('self')

    assert msg == {
            "action": "presence",
            "time": int(time()),
            "type": "status",
            "user": {
                "account_name": 'test_user',
                "status": "i`m here!"
            }
        }


def test_connection():
    sys.argv[0] = 'test.py'
    sys.argv[1] = '127.0.0.1'
    sys.argv[2] = '7777'
    # и почему тут ошибка IndexError: list assignment index out of range?
    start = new_client.client_start()
    # не понимаю, почему мне функция позвращает всего 2 значения без порта
    assert start[0] == '127.0.0.1'
    assert start[1] == '7777'

import json
import time


def get_unix_timestamp():
    return int(time.time())


def convert_from_bytes(data):
    return json.loads(data.decode('utf-8'))


def convert_to_bytes(data):
    return str(data).encode('utf-8')


class Jim:
    def __init__(self, **kwargs):
        pass

    def __str__(self):
        pass


class JimMessage:
    _message = {}

    def __init__(self):
        self._message.update({"time": get_unix_timestamp()})

    def __str__(self):
        return json.dumps(self._message)

    def create_from_dict(self, d):
        self._message.update(d)

    def _set_action(self, action):
        self._message.update({"action": action})

    def _set_user(self, account_name, status):
        self._message.update(
            {
                "user": account_name,
                "status": status
            }
        )

    def _set_room(self, room):
        self._message.update({"room": room})


class JimPresence(JimMessage):
    def __init__(self, account_name, status):
        super().__init__()
        super()._set_action("presence")
        super()._set_user(account_name, status)


class JimProbe(JimMessage):
    def __init__(self):
        super().__init__()
        super()._set_action("probe")


class JimMsg(JimMessage):
    def __init__(self):
        super().__init__()
        super()._set_action("msg")

    @property
    def name(self):
        return super()._message['to']

    @property
    def message(self):
        return super()._message['message']


class JimAuthenticate(JimMessage):
    def __init__(self, account_name, status):
        super().__init__()
        super()._set_action("authenticate")
        super()._set_user(account_name, status)


class JimJoin(JimMessage):
    def __init__(self, room):
        super().__init__()
        super()._set_action("join")
        super()._set_room(room)



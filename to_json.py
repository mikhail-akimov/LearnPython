import json


def to_json(func):
    def wrapped(text):
        result = json.dumps(func(text))
        with open('text.txt', 'w', encoding='utf-8') as r:
            r.write(result)
        with open('text.txt', 'r', encoding='utf-8') as r:
            print(r.read())
        return result
    return wrapped


@to_json
def convert(text):
    print(text)
    return text


convert({1: 2, 3: 4, 7: 10, 15: 32})
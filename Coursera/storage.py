import argparse
import os
import json
import tempfile

parser = argparse.ArgumentParser()
parser.add_argument("--key", help="Enter key to store")
parser.add_argument("--value", help="Enter value for this key")
args = parser.parse_args()

storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')


def read():
    try:
        with open(storage_path, 'r', encoding='utf-8') as ro:
            result = json.loads(ro.read())
            return result
    except FileNotFoundError:
        with open(storage_path, 'w', encoding='utf-8') as cr:
            d = {}
            cr.write(json.dumps(d))
        with open(storage_path, 'r', encoding='utf-8') as ro:
            return ro.read()


def write(line_to_write):
    with open(storage_path, 'w', encoding='utf-8') as w:
        line = json.dumps(line_to_write)
        w.write(line)
        print('saved...')


if args.key and not args.value:
    print(read().get(args.key))
else:
    d = read()
    try:
        if d.get(args.key) is None:
            d[args.key] = str(args.value)
        else:
            new_value = str(d.get(args.key) + ', ' + args.value)
            d[args.key] = new_value
    except KeyError:
        d[args.key] = str(args.value)
        print(d)
        print(type(d))
    result_w = d
    write(result_w)

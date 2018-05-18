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
            return json.loads(ro.read())
    except FileNotFoundError:
        with open(storage_path, 'w', encoding='utf-8') as cr:
            d = {}
            cr.write(json.dumps(d))
        with open(storage_path, 'r', encoding='utf-8') as ro:
            return ro.read()


def write(line_to_write):
    with open(storage_path, 'w', encoding='utf-8') as w:
        w.write(json.dumps(line_to_write))


if args.key and not args.value:
    print(read()[args.key])
else:
    d = read()
    if d[args.key] is None:
        d[args.key] = args.value
    else:
        d[args.key] = d[args.key] + ', ' + args.value
    write(d)


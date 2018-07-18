import sys

count = int(sys.argv[1])

for i in range(count):
    i += 1
    print((count - i) * " " + "#" * i)
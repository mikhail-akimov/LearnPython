import tempfile
import os


class File:
    def __init__(self, path):
        self.path = path
        self.current = 0
        self.stop = 0

    def write(self, text):
        self.text = text

        with open(self.path, 'a') as f:
            f.write('{}\n'.format(text))

    def __add__(self, t):
        new_file_path = os.path.join(tempfile.gettempdir(), 'temp.sum.file')

        with open(new_file_path, 'w') as f:
            with open(self.path) as o:
                for line_o in o.read():
                    f.write(line_o)
            with open(t.path) as t:
                for line_t in t.read():
                    f.write(line_t)

    def __iter__(self):
        with open(self.path, 'r') as f:
            self.end = len(f.readlines())
            return f.readlines()

    def __next__(self):
        if self.current >= self.end:
            raise StopIteration

        result = self.current
        self.current += 1
        return result

    def __str__(self):
        return self.path


obj = File('1.txt')
# obj.write('asdasdasd')

# first = File('1.txt')
# second = File('2.txt')

# new_obj = first + second


# Я НЕ РАЗОБРАЛСЯ С ИТЕРАТОРОМ! Вернусь к нему позже.

# print(obj)

class FileReader:
    def __init__(self, url):
        self.url = url

    def read(self, url):
        try:
            with open(url, 'r', encoding='utf-8') as r:
                return r.read()
        except IOError:
            return ""

reader = FileReader(r'C:\Users\makimov.SCLUB\PycharmProjects\LearnPython\Coursera\env\stairs.py')
print(reader.read(reader.url))

class OpenFile:
    def __init__(self, path, type):
        self.file = open(path, type, encoding='utf8')

    def __enter__(self):
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()


with OpenFile('hello.txt', 'wt') as f:
    f.write('Мой файл ')

with open('input.txt', encoding='utf8') as f:
    for line in f:
        points = int(line.split()[-1])
        if points <= 1 or points >=4:
            name = " ".join(line.split()[:-1])
            print(name)


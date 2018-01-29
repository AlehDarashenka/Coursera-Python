import tempfile
from os import path
import uuid


class File:
    def __init__(self, full_path):
        self.full_path = full_path
        self.current_position = 0



    def write(self, text):
        with open(self.full_path, 'w+') as f:
            f.write(text)

    def read(self):
        with open(self.full_path,'r+') as f:
            return f.read()

    def readline(self):
        with open(self.full_path, 'r+')as f:
            return f.readline()


    def __add__(self, other):
        storage_path = path.join(tempfile.gettempdir(), uuid.uuid4().hex)
        new_file = File(storage_path)
        text = self.read()+other.read()
        new_file.write(text)
        return new_file

    def __iter__(self):
        return self

    def __next__(self):
        with open(self.full_path, 'r+') as f:
            f.seek(self.current_position)
            line = f.readline()
            if not line:
                self.current_position = 0
                raise StopIteration("EOF")
            self.current_position = f.tell()
            return line


    def __str__(self):
        return self.full_path

if __name__=='__main__':
    a = File('D:/text1')
    a.write('Hello, Aleh!\n')
    b = File('D:/text2')
    b.write('I was wondering to know if...')
    c = a+b
    for line in c:
        print (line)



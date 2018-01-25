class FileReader:
    def __init__(self, file_path):
        self.path = file_path

    def read(self):
        try:
            with open(self.path, 'r') as f:
                return f.read()
        except IOError:
            return ""


if __name__ == '__main__':
    reader = FileReader("D:/my_file.txt")
    print(reader.read())
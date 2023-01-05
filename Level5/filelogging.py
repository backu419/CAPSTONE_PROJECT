import logging, os


class FileLog():

    def __init__(self):
        logging.basicConfig(filename="filelog.txt", level=logging.INFO)

    def find(self, filename, path):
        try:
            for root, dirs, files in os.walk(path):
                for name in files:
                    if name == filename:
                        print("File Exist ")
                        break
        except FileNotFoundError as msg:
            print(logging.exception(msg))
            print("File not found")


if __name__ == '__main__':
    obj=FileLog()
    obj.find(input("file name"), input("dir name"))

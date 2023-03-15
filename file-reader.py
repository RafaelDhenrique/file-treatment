from collections import Counter

class FileReader:
    def __init__(self, file):
        self.file = file

    def read_file(self):
        opened_file = open(self.file,'r', encoding= "UTF-8")
        opened_file = opened_file.read()
        print(opened_file)
        print(type(opened_file))
    
    def take_refs(self):
        pass

    def take_values(self):
        pass

    def create_new_file(self):
        pass





first_try = FileReader('file.txt')
first_try.read_file()

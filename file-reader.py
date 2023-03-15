from collections import Counter

class FileReader:
    def __init__(self, file):
        self.file = file


    def read_file(self):
        bar_code_list = []
        opened_file = open(self.file,'r', encoding= "UTF-8")
        opened_file = opened_file.read()
        for barcode in opened_file.split(','):
            bar_code_list.append(barcode.split())

        return bar_code_list
    
    def take_refs(self,index):
        bar_code_list = self.read_file()
        bar_code = ' '.join(bar_code_list[index])
        print(type(bar_code))
        
    def take_values(self):
        pass

    def create_new_file(self):
        pass





first_try = FileReader('file.txt')
first_try.take_refs(0)

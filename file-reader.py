import re

class FileReader:
    def __init__(self, file):
        self.file = file

    def read_file(self):
        opened_file = open(self.file, 'r', encoding="UTF-8")
        opened_file = opened_file.read()
        bar_code_list = [barcode.split() for barcode in opened_file.split(',')]

        return bar_code_list
            
    
    def validate_and_refs(self,index):
        try:
            bar_code = self.take_barcode(index)
            bar_code_pattern = re.compile('^[0-9]{13}$')
            
            if bar_code_pattern.match(bar_code):
                 ref = bar_code[9:13].ljust(13)
            else:
                raise ValueError
        except ValueError:
            print('The bar code is not valid')

        return ref

    def take_barcode(self,index):
        bar_code_list = self.read_file()
        bar_code = ' '.join(bar_code_list[index])

        return bar_code
            
    def wrote_file(self, filename,index):
        new_file = open(filename, 'x')
        myref = self.validate_and_refs(index)
        print(myref)
        
        return
    


        
            
    

first_try = FileReader('file.txt')
first_try.wrote_file('new-refs',0)

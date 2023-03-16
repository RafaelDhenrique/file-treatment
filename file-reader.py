import re

class FileReader:
    def __init__(self, file):
        self.file = file

    def read_file(self):
        opened_file = open(self.file, 'r', encoding="UTF-8")
        opened_file = opened_file.read()
        bar_code_list = [barcode.split() for barcode in opened_file.split(',')]

        return bar_code_list

    def take_refs(self, index):
        bar_code_list = self.read_file()
        bar_code = ' '.join(bar_code_list[index])
        try:
            ref = bar_code[9:13].ljust(13)
            return ref
        except IndexError:
            return print(f'O item selecionado não existe, selecione algum item da lista:{bar_code_list}')

    def validate_bar_code(self, barcode):
        bar_code_pattern = re.compile('^[0-9]{13}$')
        pass


    def take_values(self):
        pass

    def create_new_file(self):
        pass


first_try = FileReader('file.txt')
first_try.take_refs(5)

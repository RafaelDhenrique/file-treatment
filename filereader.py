import re


class FileReader:
    def __init__(self, file):
        self.file = file

    # read the file that you want work on
    def read_file(self):
        opened_file = open(self.file, 'r', encoding="UTF-8")
        opened_file = opened_file.read()
        bar_code_list = [barcode.split() for barcode in opened_file.split(',')]

        return bar_code_list

    # validade if the content in file is a realbarcode and extract the references from the right ones
    def validate_and_refs(self, index):
        try:
            bar_code = self.take_barcode(index)
            bar_code_pattern = re.compile('^[0-9]{13}$')

            if bar_code_pattern.match(bar_code):
                ref = bar_code[9:13].ljust(13)
                return ref
            else:
                raise ValueError
        except ValueError:
            print('The bar code is not valid')

    # isolate a barcode to work on
    def take_barcode(self, index):
        bar_code_list = self.read_file()
        bar_code = ' '.join(bar_code_list[index])

        return bar_code

    # create a newfile
    def create_new_file(self, filename,):
        new_file = open(filename, 'x')

        return new_file

    # wrote in file created and inser the barcode and the references
    def wrote_in_file(self, filename, index):
        file = open(filename, "a")
        contents = [self.take_barcode(index), self.validate_and_refs(index)]
        to_write = f'From the barcode:{contents[0]}  -- REF:{contents[1]}\n'
        file.write(to_write)
        file.close()

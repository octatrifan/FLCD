from symtable import SymbolTable

from lexic import Lexic


class Scanner:
    def __init__(self):
        self.st = SymbolTable()
        self.lexic = Lexic()

    def run(self, filename):
        file = open(filename, 'r')
        lines = file.readlines() 

        line_number = 0
        for line in lines:
            line_number+=1
            tokens = self.lexic.tokenize(line, line_number)
            #TODO: Check if token is identifier or constant and add it into the symbol Table

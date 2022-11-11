from operator import truediv
from textwrap import indent
import re
from tracemalloc import start

class Lexic:
    def __init__(self):
        self.separators = ["[","]","(",")","{","}",";"]
        self.special_characters = ['+', '-', '*', '/', '>', '=', '<', '(', ')', '[', ']', '{', '}', ';', ' ', '.', '!', '"', ',']
        self.reserved_words = ["array", "int", "float", "string", "char", "bool", "if", "otherwise", "read", "print", "length", "while", "for", "do"]
        self.__split_regex = "(;|,|>=|<=|==|!=|\*\*|\*|>|<|%|\\+|-|=| |\(|\)|:|\{|\}|\[|\])"

    def show_error(self, error, line):
        print("ERROR! Line: "+ str(line) + " - " + str(error))    

    def check_number(self, number):
        try:
            float(number)
            return True
        except Exception:
            return False    

    def check_identifier(self, identifier):
        if len(identifier) > 10 or len(identifier) < 1:
            raise SyntaxError("Invalid indentifier length")
        if identifier in self.reserved_words:
            raise SyntaxError("Invalid identifier: " + identifier + " - must not be a reserved word")
        
        pattern = "^[A-Za-z0-9_]*$"
        if not bool(re.match(pattern, identifier)):
            raise SyntaxError("Invalid char in indentifier "+ identifier)
        if not identifier[0].isalpha():
            raise SyntaxError("Identifier must begin with letter")    

    def check_constant(self, constant):
        if constant=="false" or constant=="true":
            return True
        if len(constant)>=2 and constant[0] == constant[len(constant)-1] == '"':
            return True
        if len(constant) < 1:
            return False
        if self.check_number(constant):
            return True
        return False

    def check_is_valid_char(self, char):
        if char.isalpha() or char.isdigit() or char in self.special_characters or char=='\n':
            return True
        return False

    def extract_strings(self, line, line_number):
        string_constants = []
        positions = [pos for pos, char in enumerate(line) if char == '"']
        if(len(positions)%2==1):
            raise SyntaxError("ERROR at line " + str(line_number) + " - No ending quotes!")
        for i in range(len(positions)-1):
            string_constants.append((line[positions[i]:positions[i+1]+1], positions[i], positions[i+1]))
        return string_constants

    def tokenize(self, line, line_number):
        tokens = []
        if "//" in line:
            pos = line.find("//")
            line = line[:pos]

        string_tokens = self.extract_strings(line, line_number)
        for (string, start_pos, end_pos) in string_tokens:
            string = string.replace(" ","~")

            line = line[:start_pos]+ string + line[end_pos+1:]
        line_stripped = line.strip()
        line_stripped = re.split(self.__split_regex, line_stripped)
        for token in line_stripped:
            if token!=' ' and token!='':
                token = token.replace("~", " ")
                tokens.append(token)
        return tokens       
                
                    



                

            


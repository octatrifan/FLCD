from operator import truediv
from textwrap import indent
import re

class Lexic:
    def __init__(self):
        self.separators = ["[","]","(",")","{","}",";"]
        self.special_characters = ['+', '-', '*', '/', '>', '=', '<', '(', ')', '[', ']', '{', '}', ';', ' ', '.', '!']
        self.reserved_words = ["array", "int", "float", "string", "char", "bool", "if", "otherwise", "read", "print", "length", "while", "for", "do"]

    def show_error(self, error, line):
        print("ERROR! Line: "+ line + " - " + error)    

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
        # TODO: add the checks for constant
        if len(constant) < 1:
            raise SyntaxError("Invalid constant length")

    def check_is_valid_char(self, char):
        if char.isalpha() or char.isdigit() or char in self.special_characters:
            return True
        return False

    def parse_string(self, line, position):
        token = '\"'
        position+=1
        char = line[position]
        while char!='\"':
            if not self.check_is_valid_char(char):
                raise SyntaxError("Invalid char")
            token += char
            position+=1
            if position==len(line):
                raise Exception("No ending quotes!") 
            char = line[position]
        token += '\"'
        position+=1
        return token, position

    def parse_signed_number(self, line, position):
        pass    

    def tokenize(self, line):
        tokens = []
        position = 0
        for char in line:
            if not self.check_is_valid_char(char):
                raise SyntaxError("Invalid char - does not exist in alphabet")

            try:           
                if char == '\"':
                    token, pos = self.parse_string()
                elif pos > 1 and (char == "+" or char == "-") and line[pos+1].isdigit():
                    token, pos = self.parse_signed_number()
                elif True: # TODO: add all other conditions
                    pass
            except Exception as e:
                self.show_error(e, line)

            


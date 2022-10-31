import sys
from Scanner.lexic import Lexic
from Scanner.data.pif import PIF
from Scanner.data.st import SymbolTable


class Scanner:
    def __init__(self):
        self.st = SymbolTable()
        self.pif = PIF()
        self.lexic = Lexic()
        self.reserved_tokens = []

    def run(self, filename):
        try:
            self.run_tokenizer(filename)
        except Exception as e:
            print(str(e))    

    def run_tokenizer(self, filename):
        reserved_tokens_file = open("Input/token.in", 'r')
        lines = reserved_tokens_file.readlines() 
        for line in lines:
            self.reserved_tokens.append(line.strip())

        file = open(filename, 'r')
        lines = file.readlines()     
        line_number = 0
        for line in lines:
            line_number+=1
            tokens = self.lexic.tokenize(line, line_number)
            i=0
            while i < len(tokens):
                if tokens[i] in self.reserved_tokens:
                    if (tokens[i]=="<" or tokens[i]==">") and tokens[i+1]=="=":
                        self.pif.add_token((tokens[i]+tokens[i+1]))
                        i+=1
                    elif tokens[i]=="-" or tokens[i]=="+":
                        if i==0 or i==len(tokens)-1:
                            raise Exception("Error at line: "+str(line_number)+" Invalid placement of + -")    
                        if not self.lexic.check_number(tokens[i-1]) and self.lexic.check_number(tokens[i+1]):
                            pos = self.st.insert((tokens[i]+str(tokens[i+1])))
                            self.pif.add_constant(pos) 
                            i+=1
                    else:
                        self.pif.add_token(tokens[i])    
                elif self.lexic.check_constant(tokens[i]):
                    pos = self.st.insert(tokens[i])
                    self.pif.add_constant(pos) 
                else: 
                    try:
                        self.lexic.check_identifier(tokens[i])
                    except Exception as e:
                        raise Exception("ERROR at line: "+str(line_number)+" - " + str(e))
                    pos = self.st.insert(tokens[i])
                    self.pif.add_identifier(pos) 
                i+=1    

        with open('Output/pif.out', 'w') as f:
            for line in self.pif.map:
                f.write(f"{line}\n")
        with open('Output/st.out', 'w') as f:
            f.write("Symbol Table is implemented as a Hash Table\n")
            for i in range(len(self.st.symboltable.data)):
                if self.st.symboltable.data[i] is not None:
                    line = "Pos "+str(i)+" : "+self.st.symboltable.data[i]
                    f.write(f"{line}\n")
        print("Lexically correct")            

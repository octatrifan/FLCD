from hashtable import HashTable

class SymbolTable:
    def __init__(self):
        self.symboltable = HashTable(10)

    def insert(self, value):
        return self.symboltable.insert(value)
    
    def get_pos(self, value):
        return self.symboltable.get_pos(value)




    


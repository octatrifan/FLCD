from hashtable import HashTable

class SymbolTable:
    def __init__(self):
        self.symboltable = HashTable(10)

    def insert(self, value):
        return self.symboltable.insert(value)
    
    def get_pos(self, value):
        return self.symboltable.get_pos(value)

class Tests:
    def test_st(self):
        symboltable = SymbolTable()
        symboltable.insert("octa")
        symboltable.insert("trifan")
        symboltable.insert("alex")
        symboltable.insert("ion")
        symboltable.insert("nelu")
        assert(symboltable.get_pos("octa")!=-1)
        assert(symboltable.get_pos("nelu")!=-1)
        assert(symboltable.get_pos("nimeni")==-1)


        print("\nTest Symbol Table passed\n")  

    def test_with_print(self): 
        symboltable = SymbolTable()
        symboltable.insert("octa")
        symboltable.insert("trifan")
        symboltable.insert("alex")
        symboltable.insert("ion")
        symboltable.insert("nelu")


        print(symboltable.symboltable.data, "\n")
        print("Octa position: ", symboltable.get_pos("octa"))
        print("Nelu position: ", symboltable.get_pos("nelu"))
        print("Nimeni position: ", symboltable.get_pos("nimeni"))            


test = Tests()
test.test_st()
test.test_with_print()


    


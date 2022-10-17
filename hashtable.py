import hashlib

class HashTable:
    def __init__(self):
        self.size = 0
        self.capacity = 10
        self.data = [None for i in range(self.capacity)]

    def get_hash(self, value):
        hashkey = int(hashlib.md5(value.encode('utf-8')).hexdigest(), 16) % self.capacity
        return hashkey

    def insert(self, value):
        self.resize()
        hash = self.get_hash(value)
        while self.data[hash] is not None:
            if self.data[hash]==value:
                return -1
            hash+=1
            hash%=self.capacity

        self.data[hash] = value
        self.size+=1
    
    def get_pos(self, value):
        hash = self.get_hash(value)
        if self.data[hash]==value:
            return hash

        index = hash+1
        while self.data[index]!=value and index!=hash:
            index+=1
            index%=self.capacity
        if index==hash:
            return -1
        return index    


    def delete(self, value):
        hash = self.get_hash(value)
        if self.data[hash]==value:
            self.data[hash]=None
            return hash

        index = hash+1
        while self.data[index]!=value and index!=hash:
            index+=1
            index%=self.capacity
        if index==hash:
            return -1
        self.data[index]=None
        self.size-=1
        return index   

    def resize(self):
        pass    


class Tests:
    def test_1(self):
        hashtable = HashTable()
        hashtable.insert("octa")
        hashtable.insert("trifan")
        hashtable.insert("alex")
        hashtable.insert("ion")
        hashtable.insert("nelu")

        assert(hashtable.insert("octa")==-1)
        assert(hashtable.get_pos("octa")!=-1)
        assert(hashtable.get_pos("nelu")!=-1)
        assert(hashtable.get_pos("nimeni")==-1)

        print("\n Hashtable: ", hashtable.data, "\n")
        print("Octa position: ", hashtable.get_pos("octa"))
        print("Nelu position: ", hashtable.get_pos("nelu"))
        print("Nimeni position: ", hashtable.get_pos("nimeni")) 

        print("\nTest 1 passed\n")

tests = Tests()
tests.test_1()


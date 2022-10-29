import hashlib

class HashTable:
    def __init__(self, capacity):
        self.size = 0
        self.capacity = capacity
        self.data = [None for i in range(self.capacity)]

    def get_hash(self, value):
        hashkey = int(hashlib.md5(value.encode('utf-8')).hexdigest(), 16) % self.capacity
        return hashkey

    def insert(self, value):
        self.resize()
        hash = self.get_hash(value)
        while self.data[hash] is not None and self.data[hash]!=value:
            hash+=1
            hash%=self.capacity

        self.data[hash] = value
        self.size+=1
        return hash
    
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

    def get_hashtable(self):
        return self.data

    def resize(self):
        pass    

    def __str__(self) -> str:
        print(self.data)









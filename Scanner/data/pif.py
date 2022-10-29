class PIF:
    def __init__(self):
        self.map = []
    
    def add_identifier(self, position):
        self.map.append(["id", position])

    def add_constant(self, position):
        self.map.append(["const", position])    
    
    def add_token(self, token):
        self.map.append([token, -1])
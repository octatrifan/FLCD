class Node:
    def __init__(self, parent, sibling, has_right, index, value):
        self.parent = parent
        self.value = value
        self.index = index
        self.sibling = sibling
        self.has_right = has_right


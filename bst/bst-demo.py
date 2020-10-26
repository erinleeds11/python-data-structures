class Node:
    def __init__(self, key):
        self.data = key
        self.left_child = None
        self.right_child = None

class BSTDemo:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if not isinstance(key, Node):
            key = Node(key)
        
        if self.root = None:
            self.root = key
        else:
            self._insert(self.root, key)

    def  _insert(self, curr, key):
        if key.data > curr:
            if curr.right_child ==None:
                curr.right_child = key
            else:
                self._insert(curr.right_child, key)
        if key.data < curr:
            if curr.left_child == None:
                curr.left_child = key
            else:
                self._insert(curr.left_child, key)


        
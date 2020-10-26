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


    def in_order(self):
        #left, root, right
        self._in_order(self.root)
        print("")

    def _in_order(self, curr):
        if curr:
            self._in_order(curr.left_child)
            #rints in same line
            print(curr.data, end =" ")
            self._in_order(curr.right_child)
    
    def pre_order(self):
        #root, left, right
        self._pre_order(self.root)
        print("")

    def _pre_order(self, curr):
        if curr:
            print(curr.data, end =" ")
            self._in_order(curr.right_child)
            self._in_order(curr.left_child)
    
    def post_order(self):
        #left, right, root
        self._post_order(self.root)
        print("")

    def _post_order(self, curr):
        if curr:
            self._in_order(curr.left_child)
            self._in_order(curr.right_child)
            print(curr.data, end =" ")
            
        

    
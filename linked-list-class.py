class Node:

    def __init__(self, data=None):
        self.data = data
        self.next = None
    
    def __str__(self):
        return str(self.data)

class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def append_val(self, x):
        if not isinstance(x, Node):
            x = Node(x)
        if self.head == None:
            self.head = x
        else:
            self.tail.next = x
        self.tail = x
    
    def add_to_start(self, x):
        if not isinstance(x, Node):
            x = Node(x)
        x.next = self.head
        self.head = x
    
    def search_val(self, x):
        if not isinstance(x, Node):
            x = Node(x)
        curr = self.head
        idx = 0
        while curr != None:
            if curr.data == x.data:
                return idx
            idx+=1
        return "none"


    def __str__(self):
        #prints 5-->4-->2
        curr = self.head
        string = ''
        while curr != None:
            string += str(curr.data) + "-->"
            curr = curr.next

        string += "None"
        if string:
            return "["+string+"]"
        else: 
            return "[]"

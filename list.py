from node import Node

class List:
    def __init__(self):
        self.head = None
    
    def append(self, data):
        if self.head == None:
            self.head = Node(data)
        else:
            self.head.append(data)

    def count(self):
        if self.head == None:
            return 0
        else:
            return self.head.count()

    def to_string(self):
        if self.head == None:
            return ""
        else:
            return self.head.to_string()

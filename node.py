class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def append(self, data):
        if self.next == None:
            self.next = Node(data)
        else:
            self.next.append(data)

    def count(self):
        if self.next == None:
            return 1
        else:
            return 1 + self.next.count()

    def to_string(self):
        if self.next == None:
            return self.data
        else:
            return self.data + " " + self.next.to_string()

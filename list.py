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

    def insert(self, number, data):
        if self.head == None:
            self.head = Node(data)
        else:
            self.head.insert(number, data)

    def prepend(self, data):
        if self.head == None:
            self.head = Node(data)
        else:
            temp = self.head
            self.head = Node(data)
            self.head.next = temp

    def find(self, position, number):
        elements = ""
        if self.head == None:
            return elements
        else:
            current_node = self.head
            count = 1

            while count < position:
                current_node = current_node.next
                count += 1
            count = 1

            while count <= number:
                elements += current_node.data
                elements += " "
                current_node = current_node.next
                count += 1
        return elements.rstrip()

    def pop(self):
        if self.head == None:
            return None
        elif self.head.next == None:
            temp = self.head.data
            self.head = None
            return temp
        else:
            current_node = self.head
            while current_node.next.next != None:
                current_node = current_node.next
            temp = current_node.next.data
            current_node.next = None
            return temp

    def includes(self, data):
        result = False
        if self.head == None:
            return result
        current_node = self.head
        while current_node.next != None:
            if current_node.data == data:
                result = True
            current_node = current_node.next
        return result

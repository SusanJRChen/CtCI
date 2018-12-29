class Node:
    def __init__(self, value):
        self.data = value
        self.next = None
        self.prev = None

    def insertList(self, values):
        for i in values:
            self.insert(i)

    def insert(self, value):
        if self.next == None:
            self.next = Node(value)
            self.next.prev = self
        else:
            self.next.insert(value)
    
    def print(self):
        if self.next != None:
            print(self.data, end=' ')
            self.next.print()

def delete(node, value):
    if node.data == value:
        return node.next
    else:
        rest = delete(node.next, value)
        node.next = rest
        rest.prev = node
        return node

class SingleNode:
    def __init__(self, value):
        self.data = value
        self.next = None

    def insertList(self, values):
        for i in values:
            self.insert(i)

    def insert(self, value):
        if self.next == None:
            self.next = Node(value)
        else:
            self.next.insert(value)
    
    def print(self):
        if self.next != None:
            print(self.data, end=' ')
            self.next.print()
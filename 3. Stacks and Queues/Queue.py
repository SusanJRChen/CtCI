class QueueNode:
    def __init__(self, value):
        self.value = value
        self.next = None

class Queue:
    def __init__(self, value):
        self.base = QueueNode(value)
        self.top = self.base
    
    def add(self, item):
        if self.base == None:
            self.base = QueueNode(item)
            self.top = self.base
        else:
            self.top.next = QueueNode(item)
            self.top = self.top.next
    
    def remove(self):
        if self.base == None:
            return -1
        else:
            temp = self.base.value
            self.base = self.base.next
            return temp
    
    def peek(self):
        if self.top == None:
            return -1
        else:
            return self.top.value

    def isEmpty(self):
        return self.top == None
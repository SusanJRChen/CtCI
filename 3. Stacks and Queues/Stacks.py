class StackNode:
    def __init__(self,value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self, value):
        self.top = StackNode(value)

    def pop(self):
        if self.top == None:
            return None
        temp = self.top.value
        self.top = self.top.next
        return temp
    
    def push(self, item):
        if self.top == None:
            self.top = StackNode(item)
        else:
            temp = StackNode(item)
            temp.next = self.top
            self.top = temp
    
    def peek(self):
        if self.top == None:
            return None
        return self.top.value
    
    def isEmpty(self):
        return self.top == None
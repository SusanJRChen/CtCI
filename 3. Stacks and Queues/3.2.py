class StackNode:
    def __init__(self,value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self, value):
        self.top = StackNode(value)
        self.minval = [value]

    def min(self):
        return self.minval[len(self.minval) - 1]

    def pop(self):
        if self.top == None:
            return -1
        temp = self.top.value
        self.top = self.top.next

        if (self.min() == temp):
            self.minval = self.minval[:-1]

        return temp
    
    def push(self, item):
        if self.top == None:
            self.top = StackNode(item)
        else:
            temp = StackNode(item)
            self.top.next = temp
            self.top = self.top.next
            
        if self.min() > item:
            self.minval.append(item)
    
    def peek(self):
        if self.top == None:
            return -1
        return self.top.value
    
    def isEmpty(self):
        return self.top == None

a = Stack(5)
print(a.min())
a.push(3)
print(a.min())
a.pop()
print(a.min())
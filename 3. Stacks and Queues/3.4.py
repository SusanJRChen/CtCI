from Queue import Queue
from Stacks import Stack

class MyQueue:
    def __init__(self):
        self.stack1 = Stack(0)
        self.stack2 = Stack(0)
        self.stack1.pop()
        self.stack2.pop()
        self.use1 = True
    
    def add(self, value):
        if self.use1:
            self.stack1.push(value)
        else:
            self.stack2.push(value)
    
    def remove(self):
        if self.use1:
            self.use1 = not self.use1
            while (not self.stack1.isEmpty()):
                self.stack2.push(self.stack1.pop())
            return self.stack2.pop()
        else:
            self.use1 = not self.use1
            while (not self.stack2.isEmpty()):
                self.stack1.push(self.stack2.pop())
            return self.stack1.pop()

a = MyQueue()
a.add(2)
a.add(3)
a.add(5)
a.add(7)
print(a.remove())
print(a.remove())
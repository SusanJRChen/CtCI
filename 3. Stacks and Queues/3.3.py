from Stacks import *

class SetOfStacks:
    def __init__(self, capacity):
        self.capacity = 0
        self.stacks = []
        self.length = 0
        self.counter = 1
    
    def push(self, item):
        if self.length < 1:
            self.stacks.append(Stack(item))
        elif self.counter >= self.capacity:
            self.counter = 0
            self.stacks.append(Stack(item))
        else:
            self.counter += 1
            self.stacks[self.length - 1].push(item)
        self.length += 1
    
    def pop(self):
        if self.length < 1:
            return None
        else:
            temp = self.stacks[self.length - 1].pop()
            if self.stacks[self.length - 1].isEmpty():
                self.counter = self.capacity
                del self.stacks[self.length - 1]
                self.length -= 1
            else:
                self.counter -= 1
            return temp

a = SetOfStacks(3)
a.push(3)
a.push(5)
a.push(6)
a.push(7)
a.push(9)

print(a.pop())
print(a.pop()) 
print(a.pop()) 
print(a.pop())

a.push(3)
a.push(5)
a.push(6)
a.push(7)
a.push(9)

print(a.pop())
print(a.pop()) 
print(a.pop()) 
print(a.pop()) 
print(a.pop())
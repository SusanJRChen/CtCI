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
        cur = self.top
        prev = self.top
        if self.top == None:
            self.top = StackNode(item)
        else:
            while (cur != None and cur.value < item):
                prev = cur
                cur = cur.next
            temp = StackNode(item)
            temp.next = cur
            prev.next = temp
    
    def peek(self):
        if self.top == None:
            return None
        return self.top.value
    
    def isEmpty(self):
        return self.top == None

a = Stack(1)
a.push(5)
a.push(3)

print(a.pop())
print(a.pop())
print(a.pop())
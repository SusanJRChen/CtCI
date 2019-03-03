class ThreeInOne:
    def __init__(self, size, value1, value2, value3):
        self.n = size
        self.array = [None] * (self.n + 1)
        self.top1 = int(size/3)
        self.top2 = 2 * int(size/3)
        self.top3 = size
        self.array[self.top1], self.array[self.top2], self.array[self.top3] = value1, value2, value3
    
    def peek(self, stacknum):
        if stacknum > 3 or stacknum < 1: 
            return None
        if stacknum == 1:
            return self.array[self.top1]
        elif stacknum == 2:
            return self.array[self.top2]
        else:
            return self.array[self.top3]

    def push(self, stacknum, value):
        if stacknum > 3 or stacknum < 1: 
            return None
        if stacknum == 1:
            self.top1 -= 1
            self.array[self.top1] = value
        elif stacknum == 2:
            self.top2 -= 1
            self.array[self.top2] = value
        else:
            self.top3 -= 1
            self.array[self.top3] = value
    
    def pop(self, stacknum):
        if stacknum > 3 or stacknum < 1: 
            return None
        if stacknum == 1:
            if self.top1 > int(self.n/3):
                return None
            else:
                temp = self.array[self.top1]
                self.array[self.top1] = None
                self.top1 += 1
                return temp
        elif stacknum == 2:
            if self.top2 > 2 * int(self.n/3):
                return None
            else:
                temp = self.array[self.top2]
                self.array[self.top2] = None
                self.top2 += 1
                return temp
        else:
            if self.top3 > self.n:
                return None
            else:
                temp = self.array[self.top3]
                self.array[self.top3] = None
                self.top3 += 1
                return temp

a = ThreeInOne(99, 11, 22, 33)
a.push(2, 24)
print(a.peek(1))
print(a.pop(2), a.peek(2))
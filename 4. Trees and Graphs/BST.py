class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = self.left
    
    def DFS(self, value):
        print(self.value, end=" ")
        if (self.value == value):
            return True
        a = False
        b = False
        if self.left != None:
            a = self.left.DFS(value)
            if a:
                return a
        if self.right != None:
            b = self.right.DFS(value)
            if b:
                return b
        
        return False
    
    def BFS(self, value):
        # print(self.value, end=" ")
        if (self.value == value):
            return True
        if self.left != None:
            print(self.left.value, end=" ")
            if self.left.value == value:
                return True
        if self.right != None:
            print(self.right.value, end=" ")
            if self.right.value == value:
                return True
        if self.left != None:
            a = self.left.BFS(value)
            if a: return a
        if self.right != None: 
            a = self.right.BFS(value)
            if a: return a
        
        return False

    def insert(self, value):
        if value >= self.value:
            if self.right == None:
                self.right = BSTNode(value)
            else:
                self.right.insert(value)
        else:
            if self.left == None:
                self.left = BSTNode(value)
            else:
                self.left.insert(value)
    
    def delete(self, value):
        temp = None
        if value > self.value and self.right != None:
            temp = self.right
        elif value < self.value and self.left != None:
            temp = self.left
        if temp != None and temp.value == value:
            if temp.right == None and temp.left == None:
                if value > self.value: self.right = None
                else: self.left = None
                return True
            elif temp.left != None and temp.right == None:
                if value > self.value: self.right = temp.left
                else: self.left = temp.left
                return True
            elif temp.left == None and temp.right != None:
                if value > self.value: self.right = temp.right
                else: self.left = temp.right
                return True
            elif temp.right != None and temp.left != None:
                min_val = temp.min()
                val = temp.delete(min_val)
                self.value = min_val
                return val
        elif temp != None:
            return temp.delete(value)
        if value == self.value:
            if (self.right != None):
                min_val = self.right.min()
                self.right.delete(min_val)
                self.value = min_val
                return True
            elif self.left != None:
                max_val = self.left.max()
                self.left.delete(max_val)
                self.value = max_val

        return False
    
    def min(self):
        if self.left == None:
            return self.value
        else:
            return self.left.min()
    
    def max(self):
        if self.right == None:
            return self.value
        else:
            return self.right.max()

    def height(self):
        if (self.right == None and self.left != None):
            return 1 + self.left.height()
        elif (self.right != None and self.left == None):
            return 1 + self.right.height()
        elif (self.right != None and self.left != None):
            a = self.right.height()
            b = self.left.height()
            if a > b: 
                return 1 + a
            else: 
                return 1 + b
        else:
            return 0
    
    def inorder(self):
        if self.left != None:
            self.left.inorder()
        print(self.value, end=" ")
        if self.right != None:
            self.right.inorder()
    
    def preorder(self):
        print(self.value, end=" ")
        if self.left != None:
            self.left.inorder()
        if self.right != None:
            self.right.inorder()
    
    def postorder(self):
        if self.right != None:
            self.right.inorder()
        print(self.value, end=" ")
        if self.left != None:
            self.left.inorder()

a = BSTNode(50)
a.insert(30)
a.insert(70)
a.insert(20)
a.insert(40)
a.insert(60)
a.insert(80)
print(a.delete(20))
print(a.delete(70))
a.inorder()
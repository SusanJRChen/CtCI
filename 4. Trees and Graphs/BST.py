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
        if value > self.value and self.right != None:
            if self.right.value == value:
                temp = self.right
                if temp.right == None and temp.left == None:
                    self.right = None
                elif temp.left != None and temp.right == None:
                    self.right = temp.left
                elif temp.left == None and temp.right != None:
                    self.right = temp.right
                else:
                    
            else:
                self.right.delete(value)
    
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

a = BSTNode(6)
a.insert(2)
a.insert(5)
a.insert(1)
a.insert(7)
a.insert(3)

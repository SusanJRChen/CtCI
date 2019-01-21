class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = self.left
    
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

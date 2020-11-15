class BinaryTree:
    
    def __init__(self, root):
        self.key = root
        self.LeftChild = None
        self.RightChild = None

    def Insert_Node(self, newNode):
        if self.getRootValue() == None:
            self.setRootValue(newNode)
        else:
            if self.getRootValue() < newNode:
                if self.RightChild == None:
                    self.RightChild = BinaryTree(newNode)
                    print(" Right Child", self.getRightChild())
                else:
                    self.getRightChild().Insert_Node(newNode)
                    print(" Right Tree", self.getRightChild())
            else:
                if self.LeftChild == None:
                    self.LeftChild = BinaryTree(newNode)
                    print(" Left Child", self.getLeftChild())
                else:
                    self.getLeftChild().Insert_Node(newNode)
                    print(" Left Tree", self.getLeftChild())

    def getRightChild(self):
        return self.RightChild
    def getLeftChild(self):
        return self.LeftChild
    def setRootValue(self, obj):
        self.key = obj
    def getRootValue(self):
        return self.key
    
    def PreOrderTraversal(self):
        print(self.key)
        if self.LeftChild is not None:
           self.LeftChild.PreOrderTraversal()
        if self.RightChild is not None:
           self.RightChild.PreOrderTraversal()
           
    def PostOrderTraversal(self):
        if self.LeftChild is not None:
           self.LeftChild.PostOrderTraversal()
        if self.RightChild is not None:
           self.RightChild.PostOrderTraversal()
        print(self.key)

    def InOrderTraversal(self):
        if self.LeftChild is not None:
           self.LeftChild.InOrderTraversal()
        print(self.key)
        if self.RightChild is not None:
           self.RightChild.InOrderTraversal()


print("\nPlease enter 10 numbers to create Sorted Binary Tree")

b = BinaryTree(None)

for i in range(1, 10):
    num = int(input("\nEnter a number: "))
    print("root:", b.getRootValue())
    b.Insert_Node(num)

print('\n*Pre-Order*')
b.PreOrderTraversal()
print('\n*Post-Order*')
b.PostOrderTraversal()
print('\n*In-Order*')
b.InOrderTraversal()
           

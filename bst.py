class BST:
    def __init__(self,value):
        self.data = value
        self.left = None
        self.right = None

    def insert(self, value):
        #if smaller than current node, then go left
        if value < self.value:
            #if currentNode has empty space on left side, then insert :)
            if self.left is None:
                self.left = BST(value)
            else: #else keep going
                #self.left.insert(value)
                self = self.left
        else:
            if self.right is None:
                self.right = BST(value)
            else:
                self.right.insert(value)




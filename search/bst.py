class Node:
    def __init__(self, val=None):
        self.val = val
        self.left = None
        self.right = None
class BinaryTree:
    def __init__(self, root=None):
        self.root = root

    def insert(self,val):
        if not self.root:
            self.root = Node(val=val)
        elif not self.root.left:
            self.root.left = Node(val=val)
        elif not self.root.right:
            self.root.right = Node(val=val)

    def __str__(self) -> str:
        return str(self.left, self.right)


tree = BinaryTree(Node(val=1))
tree.insert(2)
tree.insert(3)
tree.insert(4)
root = tree.root.value
left = tree.root.left.value
right = tree.root.right.value


print(tree)
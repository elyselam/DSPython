class Node:
    def __init__(self,val=None):
        self.value = val
        self.left = None
        self.right = None

    def __repr__(self) -> str:
        return "BNode: {}".format(self.keys)

class BTree:

    def __init__(self, vals=None):
        self.root = None
        if vals:
            self.insert(vals)
    def insert(self, vals, index=0):
        node = None
        if index < len(vals):
            node = Node(val=vals[index])
            if not self.root:
                self.root = node
            node.left = self.insert(vals, index=index*2+1)
            node.right = self.insert(vals, index=index*2+2)
        return node

level_order = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]




tree = BTree(level_order)
root = tree.root.value
child = tree.root.left.right.left.value
print(root)
print(child)
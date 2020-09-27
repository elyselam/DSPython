class Node:
    def __init__(self, keys=None, children=None):
        self.keys = keys or []
        self.children = children or []

    def is_leaf(self):
        return len(self.children) == 0

    def __repr__(self) -> str:
        return "BNode: {}".format(self.keys)

class BTree:
    def __init__(self, t):
        self.t = t
        self.root = None

b_node = Node(keys = [1,4,8])
node_is_leaf = b_node.is_leaf()
btree = BTree(3)
btree.root = b_node
keys = btree.root.keys
print(keys)
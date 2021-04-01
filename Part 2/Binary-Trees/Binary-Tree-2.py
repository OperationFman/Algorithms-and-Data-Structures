class Node:
    def __init__(self, data = None):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root == None:
            self.root = Node(data)
            print('Root: ' + str(self.root.data))
        else:
            return self._insert(data)

    def _insert(self, data):
        pass

tree = BinaryTree()
tree.insert(9)
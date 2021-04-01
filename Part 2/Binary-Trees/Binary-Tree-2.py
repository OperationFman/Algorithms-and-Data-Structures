class Node:
    def __init__(self, data = None):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self, root):
        self.root = None

    def insert(self, data):
        if self.root == None:
            self.root = Node(data)
        else:
            return self._insert(data)

    def _insert(self, data):
        pass
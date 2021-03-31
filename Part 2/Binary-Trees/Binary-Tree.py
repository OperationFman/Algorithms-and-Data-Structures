class Node:
    def __init__(self, data = None):
        self.data = data
        self.left = None
        self.right = None

    def print(self):
        print(self.data)

class BinaryTree():
    def __init__(self, item):
        self.root = Node(item)
    
    def add(self, item):
        root = self.root
        node = Node(item)
        if root.left == None or root.right == None:
            root.right = node


node = Node(10)
node.print()

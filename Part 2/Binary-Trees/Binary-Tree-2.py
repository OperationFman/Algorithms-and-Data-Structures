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
            return self._insert(data, self.root)

    def _insert(self, item, cur_node):
        if item < cur_node.data:
            if cur_node.left == None:
                cur_node.left = Node(item)
            else:
                return self._insert(item, cur_node.left)
        elif item > cur_node.data:
            if cur_node.right == None:
                cur_node.right = Node(item)
            else:
                return self._insert(item, cur_node.right)

tree = BinaryTree()
tree.insert(9)
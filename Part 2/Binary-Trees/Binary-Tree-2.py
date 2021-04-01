class Node:
    def __init__(self, data = None):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        """Runs the root first then a private method makes in easier to recursively repeat"""
        if self.root == None:
            self.root = Node(data)
            print('Root: ' + str(self.root.data))
        else:
            return self._insert(data, self.root)

    def _insert(self, item, cur_node):
        if item < cur_node.data:
            if cur_node.left == None:
                cur_node.left = Node(item)
                print("New Left Node: " + str(cur_node.left.data))
            else:
                return self._insert(item, cur_node.left)
        elif item > cur_node.data:
            if cur_node.right == None:
                cur_node.right = Node(item)
                print("New Right Node: " + str(cur_node.right.data))
            else:
                return self._insert(item, cur_node.right)
        else: print("Node value already exists")

    def view(self):
        if self.root != None:
            return self._view(self.root)

    def _view(self, cur):
        if cur != None:
            self._view(cur.left)
            print(cur.data)
            self._view(cur.right)
            print(cur.data)

tree = BinaryTree()
tree.insert(9)
tree.insert(5)
tree.insert(11)
tree.insert(1)
tree.insert(9)

tree.view()
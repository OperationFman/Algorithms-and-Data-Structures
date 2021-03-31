class Node:
    def __init__(self, data = None):
        self.data = data
        self.left = None
        self.right = None

    def print(self):
        if self.left:
            self.left.print()
        print(self.data),
        if self.right:
            self.right.print()

    def insert(self, item):
        if self.data:
            if item < self.data:
                if self.left is None:
                    self.left = Node(item)
                else:
                    self.left.insert(item)
            elif item > self.data:
                if self.right is None:
                    self.right = Node(item)
                else:
                    self.right.insert(item)
        else:
            self.data = item

    def find(self, item):
        if item < self.data:
            if self.left is None:
                return str(item)+" Not Found"
            return self.left.find(item)
        elif item > self.data:
            if self.right is None:
                return str(item)+" Not Found"
            return self.right.find(item)
        else:
            print(str(self.data) + ' is found')
        

node = Node(10)

node.insert(5)
node.insert(15)
node.insert(6)
node.insert(1)
node.insert(8)
node.insert(12)
node.insert(18)
node.insert(17)

print(node.find(55))
print(node.find(5))

preOrder = [20, 10, 6, 3, 8, 14, 30, 24, 26]
inOrder = [3, 6, 8, 10, 14, 24, 26, 30]
postOrder = [3, 8, 6, 14, 10, 26, 24, 30, 20]

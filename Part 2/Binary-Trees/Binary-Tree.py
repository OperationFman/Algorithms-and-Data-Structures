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
        cur = self.data
        history = []
        while item != cur:
            if item < self.left.data:
                history.append(cur)
                cur = self.left.data
            elif item > self.right.data:
                history.append(cur)
                cur = self.right.data
        print(cur)
        print(history)
        

node = Node(10)

node.insert(5)
node.insert(15)
node.insert(6)
node.insert(1)
node.insert(8)
node.insert(12)
node.insert(18)
node.insert(17)

node.find(15)

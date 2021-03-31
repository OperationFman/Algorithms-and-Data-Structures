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
    
    def travPreOrder(self, root):
        result = []
        if root:
            result.append(root.data)
            result = result + self.travPreOrder(root.left)
            result = result + self.travPreOrder(root.right)
        return result
        

node = Node(10)

node.insert(5)
node.insert(15)
node.insert(6)
node.insert(1)
node.insert(8)
node.insert(12)
node.insert(18)
node.insert(17)

# print(node.find(55))
# print(node.find(5))

print(node.travPreOrder(node))

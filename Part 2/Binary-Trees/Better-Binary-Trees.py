class Node:
	def __init__(self, data = None):
		self.data = data
		self.left = None
		self.right = None
		self.parent = None

class BinaryTree:
	def __init__(self):
		self.root = None

	def insert(self,item):
		if self.root == None:
			self.root = Node(item)
		else:
			self._insert(item, self.root)

	def _insert(self, item, cur):
		if item < cur.data:
			if cur.left == None:
				cur.left = Node(item)
				cur.left.parent = cur 
			else:
				self._insert(item, cur.left)
		elif item > cur.data:
			if cur.right == None:
				cur.right = Node(item)
				cur.right.parent = cur
			else:
				self._insert(item, cur.right)
		else:
			print("Node '" + str(item) + "' already exists")

	def view(self):
		if self.root != None:
			self._view(self.root)

	def _view(self, cur):
		if cur != None:
			self._view(cur.left)
			print(str(cur.data))
			self._view(cur.right)

	def height(self):
		if self.root != None: #For Leetcode this was just root
			return self._height(self.root, 0) #For Leetcode this was just root
		else:
			return 0

	def _height(self, cur, cur_height):
		if cur == None: return cur_height #For Leetcode this remained just cur
		left_height = self._height(cur.left, cur_height + 1)
		right_height = self._height(cur.right, cur_height + 1)
		return max(left_height, right_height)

	def find(self, item):
		if self.root != None:
			return self._find(item, self.root)
		else:
			return None

	def _find(self, item, cur):
		if item == cur.data:
			return cur.data
		elif item < cur.data and cur.left != None:
			return self._find(item, cur.left)
		elif item > cur.data and cur.right != None:
			return self._find(item, cur.right)

	def search(self, item):
		if self.root != None:
			return self._search(item, self.root)
		else:
			return False

	def _search(self, item, cur):
		if item == cur.data:
			return True
		elif item < cur.data and cur.left != None:
			return self._search(item, cur.left)
		elif item > cur.data and cur.right != None:
			return self._search(item, cur.right)
		return False 

tree = BinaryTree()

tree.insert(10)
tree.insert(2)
tree.insert(8)
tree.insert(4)
tree.insert(6)
tree.insert(99)
tree.insert(5)
print("The following is the ordered print out:")
tree.view()

tree.insert(2) # Prexisiting

print("Tree height is: " + str(tree.height()))

print("Looking for node '5', found: " + str(tree.find(5)))
print("Looking for node '11', found: " + str(tree.find(11)))

print("Is '5' in the list? " + str(tree.search(5)))
print("Is '11' in the list? " + str(tree.search(11)))

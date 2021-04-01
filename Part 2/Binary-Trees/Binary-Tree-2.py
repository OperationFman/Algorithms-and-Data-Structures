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
			print("Node: " + str(item) + ". Already exists")

	def view(self):
		if self.root != None:
			self._view(self.root)

	def _view(self, cur):
		if cur != None:
			self._view(cur.left)
			print(str(cur.data))
			self._view(cur.right)

	def height(self):
		if self.root != None:
			return self._height(self.root, 0)
		else:
			return 0

	def _height(self, cur, cur_height):
		if cur == None: return cur_height
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
			return cur
		elif item < cur.data and cur.left != None:
			return self._find(item, cur.left)
		elif item > cur.data and cur.right != None:
			return self._find(item, cur.right)

	def delete_item(self, item):
		return self.delete_node(self.find(item))

	def delete_node(self, node):
		if node == None or self.find(node.value)==None:
			print("Node to be deleted not found in the tree!")
			return None 
		## -----

		# returns the node with min value in tree rooted at input node
		def min_value_node(n):
			current=n
			while current.left_child!=None:
				current=current.left_child
			return current

		# returns the number of children for the specified node
		def num_children(n):
			num_children=0
			if n.left_child!=None: num_children+=1
			if n.right_child!=None: num_children+=1
			return num_children

		# get the parent of the node to be deleted
		node_parent=node.parent

		# get the number of children of the node to be deleted
		node_children=num_children(node)

		# break operation into different cases based on the
		# structure of the tree & node to be deleted

		# CASE 1 (node has no children)
		if node_children==0:

			# Added this if statement post-video, previously if you 
			# deleted the root node it would delete entire tree.
			if node_parent!=None:
				# remove reference to the node from the parent
				if node_parent.left_child==node:
					node_parent.left_child=None
				else:
					node_parent.right_child=None
			else:
				self.root=None

		# CASE 2 (node has a single child)
		if node_children==1:

			# get the single child node
			if node.left_child!=None:
				child=node.left_child
			else:
				child=node.right_child

			# Added this if statement post-video, previously if you 
			# deleted the root node it would delete entire tree.
			if node_parent!=None:
				# replace the node to be deleted with its child
				if node_parent.left_child==node:
					node_parent.left_child=child
				else:
					node_parent.right_child=child
			else:
				self.root=child

			# correct the parent pointer in node
			child.parent=node_parent

		# CASE 3 (node has two children)
		if node_children==2:

			# get the inorder successor of the deleted node
			successor=min_value_node(node.right_child)

			# copy the inorder successor's value to the node formerly
			# holding the value we wished to delete
			node.value=successor.value

			# delete the inorder successor now that it's value was
			# copied into the other node
			self.delete_node(successor)

	def search(self,value):
		if self.root!=None:
			return self._search(value,self.root)
		else:
			return False

	def _search(self,value,cur_node):
		if value==cur_node.value:
			return True
		elif value<cur_node.value and cur_node.left_child!=None:
			return self._search(value,cur_node.left_child)
		elif value>cur_node.value and cur_node.right_child!=None:
			return self._search(value,cur_node.right_child)
		return False 
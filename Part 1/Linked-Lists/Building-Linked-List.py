class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return self.data

class LinkedList:
    def __init__(self, nodes=None):
        self.head = None
        if nodes is not None:
            node = Node(data=nodes.pop(0))
            self.head = node
            for elem in nodes:
                node.next = Node(data=elem)
                node = node.next

    def add_first(self, node):
        node.next = self.head
        node.data = node

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next


llist = LinkedList()

first_node = Node('a')
llist.head = first_node

second_node = Node('b')
third_node = Node('c')
first_node.next = second_node
second_node.next = third_node

llist.add_first('z')

print(llist)

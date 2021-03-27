class Node:
    def __init__(self, data = None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = Node()

    def addLast(self, data):
        new_node = Node(data)
        cur = self.head
        while cur.next != None:
            cur = cur.next
        cur.next = new_node

    def length(self):
        total = 0
        cur = self.head
        while cur.next != None:
            cur = cur.next
            total += 1
        return total

    def contains(self):
        elements = []
        cur = self.head
        while cur.next != None:
            cur = cur.next
            elements.append(cur)
        print(elements)

llist = LinkedList()

llist.addLast(1)
llist.addLast(2)
llist.addLast(3)

print(llist.contains())
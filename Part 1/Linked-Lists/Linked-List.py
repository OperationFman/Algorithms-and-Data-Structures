class Node:
    def __init__(self, data = None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = Node()

    def length(self):
        total = 0
        cur = self.head
        while cur.next != None:
            cur = cur.next
            total += 1
        return total

    def getIndex(self, index):
        if index >= self.length():
            print("Index out of range")
            return None
        cur = self.head
        cur_index = 0
        while True:
            cur = cur.next
            if cur_index == index:
                return cur.data
            cur_index += 1

    def deleteIndex(self, index):
        if index >= self.length():
            print("Index out of range")
            return None
        cur = self.head
        cur_index = 0
        while True:
            last_node = cur
            cur = cur.next
            if cur_index == index:
                last_node.next = cur.next
                return
            cur_index += 1

    def addFirst(self, data):
        new_node = Node(data)
        cur = self.head
        new_node.next = cur.next
        cur.next = new_node

    def addLast(self, data):
        new_node = Node(data)
        cur = self.head
        while cur.next != None:
            cur = cur.next
        cur.next = new_node

    def deleteFirst(self):
        self.deleteIndex(0)

    def deleteLast(self):
        last_index = self.length()
        self.deleteIndex(last_index - 1)

    def contains(self):
        elements = []
        cur = self.head
        while cur.next != None:
            cur = cur.next
            elements.append(cur.data)
        return elements

    def indexOf(self, item):
        cur = self.head
        total = 0
        while cur.next != None:
            cur = cur.next
            if cur.data == item:
                return total
            total += 1

    def reverse(self):
        array = self.contains()
        for _ in array:
            self.deleteFirst()
        for i in array:
            self.addFirst(i)

    def kth(self, value):
        """Apparently value should be the index but that'd just be a reversed getIndex..?"""
        endCounter = 1
        countToEnd = False
        cur = self.head
        while cur.next != None:
            cur = cur.next
            if cur.data == value:
                countToEnd = True
            if countToEnd == True:
                endCounter += 1
        return endCounter


llist = LinkedList()

llist.addLast(1)
llist.addLast(2)
llist.addLast(3)
print(llist.contains())

llist.addFirst(4)
llist.addFirst(5)
llist.addFirst(6)
print(llist.contains())

llist.deleteFirst()
print(llist.contains())

llist.deleteLast()
print(llist.contains())

print(llist.indexOf(1))

llist.reverse()
print(llist.contains())

print(llist.kth(4))
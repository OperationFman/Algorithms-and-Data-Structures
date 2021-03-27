class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return repr(self.data)

class LinkedList:
    def __init__(self):
        self.head = None

    def node(self, data):
        self.data = data
        self.next = None

    def __repr__(self):

class PriQue:
    def __init__(self):
        self.priorityArray = []

    def view(self):
        print(self.priorityArray)

    def insert(self, item):
        self.priorityArray.append(item)
        self.priorityArray.sort
    
pq = PriQue()

pq.insert(1)
pq.insert(3)
pq.insert(2)
pq.insert(9)
pq.insert(4)
pq.view()
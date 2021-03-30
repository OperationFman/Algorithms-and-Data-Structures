class PriQue:
    def __init__(self):
        self.priorityArray = []

    def view(self):
        print(self.priorityArray)

    def insert(self, item):
        if self.priorityArray == []:
            self.priorityArray.append(item)
        else:
            for i in self.priorityArray:
                if item >= i:
                    print('hit')
                    index = self.priorityArray.index(i) + 1
                    self.priorityArray.insert(index, item)
    
pq = PriQue()
pq.view()

pq.insert(1)
pq.insert(3)
pq.insert(2)
pq.insert(9)
pq.insert(4)
pq.view()
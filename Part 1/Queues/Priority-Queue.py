class PriQue:
    def __init__(self):
        self.priorityArray = []

    def view(self):
        print(self.priorityArray)

    def insert(self, item):
        # self.priorityArray.append(item)
        # self.priorityArray.sort
        if self.priorityArray == []:
            self.priorityArray.append(item)
        else:
            for i in self.priorityArray:
                if item <= i:
                    self.priorityArray.insert(self.priorityArray.index(i), item)
                    break
                else:
                    self.priorityArray.append(item)
                    break
    
pq = PriQue()

pq.insert(5)
pq.insert(1)
pq.insert(2)
pq.insert(9)
pq.insert(4)
pq.insert(4)
pq.insert(0)
pq.insert(15)
pq.view()

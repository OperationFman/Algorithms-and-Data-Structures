class PriQue:
    def __init__(self):
        self.priorityArray = []

    def view(self):
        print(self.priorityArray)

    def insert(self, item):
        count = 0
        if self.priorityArray == False:
            self.priorityArray.append(item)
        for i in self.priorityArray:
            if item >= i:
                self.priorityArray.insert(count, item)
                print('hit')
                break
            else:
                count += 1
    
pq = PriQue()
pq.view()

pq.insert(1)
pq.insert(3)
pq.insert(2)
pq.insert(9)
pq.insert(4)
pq.view()
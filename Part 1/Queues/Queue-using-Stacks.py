class QuS:
    """Not allowed to select the first item, at all, only end ones"""
    def __init__(self, stack1 = [], stack2 = []):
        self.stack1 = stack1
        self.stack2 = stack2

    def viewStacks(self):
        print(self.stack1)
        print(self.stack2)

    def selectStack1First(self):
        iterations = len(self.stack1) - 1
        count = 0
        while count < iterations:
            count += 1
            i = self.stack1.pop()
            self.stack2.append(i)
        firstValue = self.stack1[-1]
        for _ in range(len(self.stack2)):
            j = self.stack2.pop()
            self.stack1.append(j)
        return firstValue

qus = QuS()
qus.stack1 = [10, 20, 30, 40, 50]

print(qus.selectStack1First())
qus.viewStacks()

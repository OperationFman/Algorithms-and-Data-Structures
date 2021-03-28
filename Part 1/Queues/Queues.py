class Queue:
    def __init__(self):
        self.array = [2, 4, 6, 8, 10]

    def view(self):
        print(self.array)

    def reverse(self, queue):
        result = []
        for i in queue[::-1]:
            result.append(i)
        return result

    def dequeue(self, item):
        self.array.append(item)

    def peek(self):
        return self.array[-1]

    def isEmpty(self):
        if self.array:
            return False
        return True

    def pointers(self, start, end):
        selection = self.array[start:end]
        return selection

queue = Queue()
# print(queue.reverse(list))

queue.dequeue(12)
queue.view()

print(queue.peek())

print(queue.isEmpty())

print(queue.pointers(1, 4))
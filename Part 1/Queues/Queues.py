class Queue:
    def reverse(self, queue):
        result = []
        for i in queue[::-1]:
            result.append(i)
        return result

queue = Queue()
list = [2, 4, 6, 8, 10]
print(queue.reverse(list))

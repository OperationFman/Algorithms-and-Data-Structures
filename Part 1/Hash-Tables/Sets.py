class Set():
    def makeSet(self, array):
        result = []
        for i in array:
            if i not in result:
                result.append(i)
        return result

miniSet = Set()

array = [1, 1, 2, 3, 4, 4, 4, 5, 6, 7, 7, 7, 8, 9, 10]
print(miniSet.makeSet(array))
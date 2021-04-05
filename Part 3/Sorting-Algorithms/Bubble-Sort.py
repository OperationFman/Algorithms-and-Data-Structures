class BubbleSort:
    def ascending(self, array):
        sort = False
        counter = 0
        for _ in range(len(array) - 1):
            if array[counter] > array[counter + 1]:
                pop = array.pop(counter)
                array.insert(counter + 1, pop)
                sort = True
            counter += 1
        if sort == True:
            self.ascending(array)
        return array

sort = BubbleSort()
array = [6,4,2,8,40,0,5,9,1]

print(sort.ascending(array))
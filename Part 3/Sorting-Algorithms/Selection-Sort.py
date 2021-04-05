class SelectionSort:
    def ascending(self, array):
        sortedArray = []
        while array != []:
            lowest = array.pop(self.getLowest(array))
            sortedArray.append(lowest)
        print(sortedArray)

    
    def getLowest(self, array):
        lowest = array[0]
        for i in array:
            if i < lowest:
                lowest = i
        return array.index(lowest)


sort = SelectionSort()
array = [6,4,2,8,40,0,5,9,1]

sort.ascending(array)
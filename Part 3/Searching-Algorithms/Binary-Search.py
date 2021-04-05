# Recursion and iteration hybrid
class BinarySearch:
    def search(self, array, lower, higher, value):
        if higher >= lower:
            middle = (higher + lower) // 2
            if array[middle] == value:
                return middle
            elif array[middle] > value:
                return self.search(array, lower, middle - 1, value)
            else:
                return self.search(array, middle + 1, higher, value)
        else:
            return None
 
binary = BinarySearch()
array = [1, 6, 2, 7, 1, 5, 9, 11, 6, 12, 3]
value = 3 # Search with this value

result = binary.search(array, 0, len(array) - 1, value)
 
if result != None:
    print("Value at index: ", str(result))
else:
    print("Value not in the array")
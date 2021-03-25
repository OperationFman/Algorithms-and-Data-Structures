array1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
array2 = [77, 2390, 783493, 3632, 2, 67, 9, 10, 50000]

# 1 Get largest number
def largestItem(array):
    return max(array)
# print(largestItem(array1))
# print(largestItem(array2))

# Find only elements in both arrays
def listIntersection(array1, array2):
    return list(set(array1) & set(array2))
# print(listIntersection(array1, array2))

# Reverse an array
def invertArray(array):
    invertedArray = []
    for i in array:
        invertedArray.insert(0, i)
    return invertedArray
# print(invertArray(array1))
# print(invertArray(array2))

def insertAtIndex(array, item, index):
    array.insert(index, item)
    print(array)
# insertAtIndex(array1, 696969, 3)
# insertAtIndex(array2, 1, 25)
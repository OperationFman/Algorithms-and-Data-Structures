# Make array, no memory allocation needed
array = []

# Insert elements to the end
array.append(1)
array.append(69)
array.append(420)

#Show what's in the array and at index 1
print(array)
print(array.index(69))

# Change element at index 1 and print it
array[1] = 96
print(array[1])

# Removes element at array index 0
array.pop(0)
print(array)

def removeIndex(index):
    try:
        array.pop(index)
    except IndexError:
        print('Index out of range')
removeIndex(2)

array.insert(1, 9000)
print(array)
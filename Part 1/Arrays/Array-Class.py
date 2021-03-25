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

# Check if index exists before popping, throws error if it doesn't
def removeIndex(index):
    try:
        array.pop(index)
    except IndexError:
        print('Index out of range')
removeIndex(2)

# Insert an element at a given index and move everything else up
# If it's too high it'll just go on the end, swell!
array.insert(1, 9000)
print(array)
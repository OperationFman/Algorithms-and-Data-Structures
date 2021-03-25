# O(logn) is a method of using logorithmic time to find something in an array.

# For example:
array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#We ant to find 10
#If using linear search we go 1, 2, 3, etc meaning it will take 10 operations to find 10

#Log n checks the middle item and checks if the desired variable is higher or lower
# 10 is higher than 5 so we don;lt check 1-4 ever again
#Repeat the step at 8 and the remaining is 9 and 10 so we found it, in 3 operations.

# O9Logn) is much much faster at scale
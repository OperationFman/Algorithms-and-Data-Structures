# O(n^2) or O of n squared is when you iterate over an array within another array, in large datasets these are slower

def Onsquared(array1, array2):
    for i in array1:
        for j in array2:
            print(i, ':', j)

Onsquared([2,4,6,8,10], ['hey', 'ho', 'here', 'we', 'go'])
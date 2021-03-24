# O(n) is linearly affected by the size of the input. In this case every item is printed so each takes '1' time

def On(array):
    for i in array:
        print(i)

On([10, 4, 88, 29, 84, 10, 0, 7])
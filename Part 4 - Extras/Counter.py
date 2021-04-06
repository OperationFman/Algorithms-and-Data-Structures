from collections import Counter

array = [1, 2, 3, 6, 2, 4, 8, 1, 7, 2, 5, 1, 0, 1, 2, 6, 2, 5]

count = dict(Counter(array))

print('Print Counter cleanly:')
print(count)

print('Loop through above dict:')
for key in count:
    print(key, count[key])

print('Loop via order of indexes:')
for key, value in enumerate(count):
    print(key, value)
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

print('Get most common value')
counter = Counter(array)
commons = counter.most_common()
# Result: [(2, 5), (1, 4), (6, 2), (5, 2), (3, 1), (4, 1), (8, 1), (7, 1), (0, 1)]
common_pair = commons[0] # Result (2, 5)
common_value = commons[0][0] # Result = 2
most_commons_count = commons[0][1] # Result = 5
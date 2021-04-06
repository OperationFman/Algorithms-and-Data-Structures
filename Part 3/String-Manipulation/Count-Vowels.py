vowels = ['a', 'e', 'i', 'o' 'u']
string = 'Hello there, General kenobi'.lower()
counter = 0

for i in string:
    if i in vowels:
        counter += 1

print('Found ' + str(counter) + ' vowels')
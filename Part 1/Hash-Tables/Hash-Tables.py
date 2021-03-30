
class Hash:
    def firstNonRepeated(self, string):
        string = string.replace(" ", "")
        # memory = {}
        for char in string:
            counter = string.count(char)
            # memory[char] = counter
            if counter == 1:
                return char

    def firstRepeated(self, string):
        string = string.replace(" ", "")
        for char in string:
            counter = string.count(char)
            if counter >= 2:
                return char

hash = Hash()
string = 'general kenobi'

print(hash.firstNonRepeated(string))
print(hash.firstRepeated(string))
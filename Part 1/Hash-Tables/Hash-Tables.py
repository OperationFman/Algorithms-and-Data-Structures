
class Hash:
    def firstNonRepeated(self, string):
        string = string.replace(" ", "")
        # memory = {}
        for char in string:
            counter = string.count(char)
            # memory[char] = counter
            if counter == 1:
                return char

hash = Hash()
string = 'hello there'

print(hash.firstNonRepeated(string))
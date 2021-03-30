from collections import Counter

class Hash:
    def firstNonRepeated(self, string):
        string = string.replace(" ", "")
        memory = Counter(string)
        print(memory)

hash = Hash()
string = 'hello there'

hash.firstNonRepeated(string)
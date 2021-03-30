class Hash:
    def firstNonRepeated(self, string):
        string = string.replace(" ", "")
        memory = {}
        for char in string:
            memory[char] = ""

        print(memory)

hash = Hash()
string = 'hello there'

hash.firstNonRepeated(string)
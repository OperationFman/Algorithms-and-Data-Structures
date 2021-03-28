class Stack:
    def reverseString(self, string):
        if type(string) is str:
            return string[::-1]
        return 'Error: Not a string'



stack = Stack()
print(stack.reverseString('Hello there'))

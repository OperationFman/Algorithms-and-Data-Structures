class Stack:
    def reverseString(self, string):
        if type(string) is str:
            return string[::-1]
        return 'Error: Not a string'

    def balancedExpression(self, string):
        stack = []
        openBrackets = ['(', '{', '[', '<']
        closeBrackets = [')', '}', ']', '>']
        for i in string:
            if i in openBrackets:
                stack.append(i)
            if i in closeBrackets:
                c = closeBrackets.index(i)
                o = openBrackets[c]
                if o != stack[-1]:
                    return 'String is not balanced'
                stack.pop()
        if stack == False:
            return 'String is balanced'
        return 'String is not balanced'
            



stack = Stack()
# print(stack.reverseString('Hello there'))

print(stack.balancedExpression('(hi)'))

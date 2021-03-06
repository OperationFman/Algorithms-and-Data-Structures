class Stack:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def view(self):
        print(self.stack1)
        print(self.stack2)

    def reverseString(self, string):
        if type(string) is str:
            return string[::-1]
        return 'Error: Not a string'

    def balancedExpression(self, string):
        try:
            stack = []
            openBrackets = ['(', '{', '[', '<']
            closeBrackets = [')', '}', ']', '>']
            for i in string:
                if i in openBrackets:
                    stack.append(i)
                if i in closeBrackets:
                    c = closeBrackets.index(i)
                    if openBrackets[c] not in stack:
                        return False
                    if openBrackets[c] == stack[-1]:
                        stack.pop()
            if stack == []:
                return 'String is balanced'
            else:
                return 'String is not balanced'
        except IndexError:
            return 'String is not balanced'

    def push1(self, value):
        self.stack1.append(value)

    def push2(self, value):
        self.stack2.append(value)



stack = Stack()
print(stack.reverseString('Hello there'))
print(stack.balancedExpression('(1 + 2 + (3 x b) = [a] / [c]) + <5>'))

stack.push1('hello')
stack.push1('there')
stack.push2('general')
stack.push2('kenobi')
stack.view()

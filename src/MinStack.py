class MinStack:

    def __init__(self):
        self.min_stack = []
        self.stack = []

    def push(self, x):
        if len(self.min_stack) > 0:
            a = self.min_stack[len(self.min_stack) - 1]
            self.min_stack.append(min(a, x))
        else:
            self.min_stack.append(x)
        self.stack.append(x)

    def pop(self):
        self.stack.pop()
        self.min_stack.pop()

    def top(self):
        return self.stack[len(self.stack) - 1]

    def getMin(self):
        return self.min_stack[len(self.min_stack) - 1]


minStack = MinStack()
minStack.push(-2)
minStack.push(-3)
minStack.push(0)

print(minStack.getMin())
minStack.pop()
print(minStack.getMin())
minStack.pop()
print(minStack.getMin())
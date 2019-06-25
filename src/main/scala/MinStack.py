class MinStack:
    def __init__(self):
        self.min_val = 0
        self.stack = []

    def push(self, x):
        if len(self.stack) == 0:
            self.stack.append(x)
            self.min_val = x
        elif x < self.min_val:
            y = 2 * x - self.min_val
            self.stack.append(y)
            self.min_val = x
        else:
            self.stack.append(x)

    def pop(self):
        if len(self.stack) == 0:
            return
        y = self.stack.pop()
        if y < self.min_val:
            self.min_val = 2 * self.min_val - y


    def top(self):
        return self.stack[len(self.stack) - 1] if len(self.stack) > 0 else None

    def getMin(self):
        if len(self.stack) == 0:
            return None
        return self.min_val


minStack = MinStack()
minStack.push(-2)
minStack.push(-3)
minStack.push(0)

print(minStack.getMin())
minStack.pop()
print(minStack.getMin())
minStack.pop()
print(minStack.getMin())
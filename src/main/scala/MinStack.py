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
        if self.stack[len(self.stack) - 1] < self.min_val:
            return self.min_val
        return self.stack[len(self.stack) - 1]

    def getMin(self):
        if len(self.stack) == 0:
            return None
        return self.min_val


minStack = MinStack()

#["MinStack","push","push","push","top","pop", "getMin", "pop"  ,"getMin",  "pop",  "push",  "top",  "getMin",  "push",  "top","getMin","pop","getMin"]
#[[],[2147483646],[2147483646],[2147483647],[],[],[],[],[],[],[2147483647],[],[],[-2147483648],[],[],[],[]]

minStack.push(2147483646)
minStack.push(2147483646)
minStack.push(2147483647)

print(minStack.top())

minStack.pop()

print(minStack.getMin())

minStack.pop()

print(minStack.getMin())

minStack.pop()

minStack.push(2147483647)
print(minStack.top())
print(minStack.getMin())

minStack.push(-2147483648)
print(minStack.top())
print(minStack.getMin())

minStack.pop()
print(minStack.getMin())
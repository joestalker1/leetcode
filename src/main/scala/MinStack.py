class MinStack(object):

    def __init__(self):
        self.st = []
        self.min = None

    def push(self, val):
        if not self.st:
            self.st.append(val)
            self.min = val
        elif val < self.min:
            enc = 2 * val - self.min
            # min = 2 * val - enc
            self.st.append(enc)
            self.min = val
        else:
            self.st.append(val)

    def pop(self):
        if not self.st:
            return
        x = self.st.pop()
        if x < self.min:
            self.min = 2 * self.min - x

    def top(self):
        if not self.st:
            return None
        if self.st[-1] < self.min:
            return self.min
        return self.st[-1]

    def getMin(self):
        if not self.st:
            return None
        return self.min

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
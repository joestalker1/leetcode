class TwoStacks:
    def __init__(self, n):
        self.arr = [0] * n
        self.p1 = 0
        self.p2 = n - 1


    def push1(self, a):
        if self.p1 > self.p2:
            raise Exception('No space in stack1')
        self.arr[self.p1] = a
        self.p1 += 1

    def push2(self, a):
        if self.p1 > self.p2:
            raise Exception('No space in stack2')
        self.arr[self.p2] = a
        self.p2 -= 1

    def pop1(self):
        if self.p1 == 0:
            raise Exception('Stack1 is empty')
        self.p1 -= 1
        a = self.arr[self.p1]
        return a

    def pop2(self):
        if self.p2 == len(self.arr) - 1:
            raise Exception('Stack2 is empty')
        self.p2 += 1
        a = self.arr[self.p2]
        return a


stack = TwoStacks(5)
stack.push1(1)
stack.push1(2)
stack.push1(3)
stack.push2(5)
stack.push2(4)

print(stack.pop1())
print(stack.pop1())
print(stack.pop1())
print(stack.pop2())
print(stack.pop2())

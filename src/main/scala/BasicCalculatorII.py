class Solution:
    def prec(self, op):
        if op == '+' or op == '-':
            return 0
        return 1

    def eval(self, stack, ops):
        while len(stack) > 0:
            zn = stack.pop()
            a = ops.pop()
            b = ops.pop()
            if zn == '+':
                ops.append(a + b)
            elif zn == '-':
                ops.append(b - a)
            elif zn == '*':
                ops.append(a * b)
            else:
                ops.append(b // a)
        return ops.pop()

    def postfix(self, s):
        j = 0
        stack = []
        buf = []
        while j < len(s):
            if '0' <= s[j] <= '9':
                i = j
                while i < len(s) and '0' <= s[i] <= '9':
                    i+= 1
                buf.append(s[j:i])
                j = i
            else:
                if s[j] in ['+','-','*','/']:
                    while len(stack) > 0 and self.prec(s[j]) <= self.prec(stack[len(stack) - 1]):
                        buf.append(stack.pop())
                    stack.append(s[j])
                j += 1
        while len(stack) > 0:
            buf.append(stack.pop())
        return buf

    def calculate(self, s):
        if not s:
            return None
        stack = []
        postfix = self.postfix(s)
        i = 0
        while i < len(postfix):
            x = postfix[i]
            if x.isdecimal():
                stack.append(int(x))
            else:
                a = stack.pop()
                b = stack.pop()
                if x == '+':
                    stack.append(a + b)
                elif x == '-':
                    stack.append(b - a)
                elif x == '*':
                    stack.append(a * b)
                else:
                   stack.append(b // a)
            i += 1
        return stack.pop()


        return self.eval(stack, ops)


sol = Solution()
print(sol.calculate("1*2-3/4+5*6-7*8+9/10"))
print(sol.calculate("3+2*2"))
print(sol.calculate(" 3+5 / 2 "))
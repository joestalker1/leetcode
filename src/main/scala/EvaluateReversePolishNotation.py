class Solution:
    def evalRPN(self, tokens):
        if not tokens:
            return None
        def eval(pos = 0, stack = []):
            if pos == len(tokens):
                return stack.pop()
            ch = tokens[pos]
            if ch == '+':
                a = stack.pop()
                b = stack.pop()
                stack.append(a + b)
            elif ch == '*':
                a = stack.pop()
                b = stack.pop()
                stack.append(a * b)
            elif ch == '-':
                b = stack.pop()
                a = stack.pop()
                stack.append(a - b)
            elif ch == '+':
                a = stack.pop()
                b = stack.pop()
                stack.append(a + b)
            elif ch == '/':
                b = stack.pop()
                a = stack.pop()
                stack.append(int(a / b))
            else:
                stack.append(int(ch))
            return eval(pos + 1)
        return eval(0)


sol = Solution()
print(sol.evalRPN(["4","13","5","/","+"]))
print(sol.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))
print(sol.evalRPN(["0","3","/"]))
print(sol.evalRPN(["2", "1", "+", "3", "*"]))



class Solution:
    def isValid(self, s):
        if not s or len(s) == 0:
            return True
        stack = []
        i = 0
        while i < len(s):
            if s[i] == '(':
                stack.append(')')
            elif s[i] == '[':
                stack.append(']')
            elif s[i] == '{':
                stack.append('}')
            else:
                ch = stack.pop()
                if s[i] != ch:
                    return False
            i += 1
        return True

sol = Solution()
print(sol.isValid("()[]{}"))
print(sol.isValid("([)]"))
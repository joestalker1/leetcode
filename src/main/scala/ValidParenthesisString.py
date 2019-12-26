class Solution:
    def checkValidString(self, s):
        if not s:
            return True
        left = []
        star = []
        for i in range(len(s)):
            if s[i] == '(':
                left.append(i)
            elif s[i] == ')':
                if left:
                    left.pop()
                elif star:
                    star.pop()
                else:
                    return False
            else:
                star.append(i)
        while len(left) > 0 and len(star) > 0:
            if star[-1] > left[-1]:
                left.pop()
                star.pop()
            else:
                break
        return len(left) == 0



sol = Solution()
print(sol.checkValidString("(((((*(()((((*((**(((()()*)()()()*((((**)())*)*)))))))(())(()))())((*()()(((()((()*(())*(()**)()(())"))#false
print(sol.checkValidString("(*()"))#true
print(sol.checkValidString("((***"))#true
print(sol.checkValidString("***))"))#true
print(sol.checkValidString("(()) ((())()()(*)(*()(())())())()()((()())((()))(*"))#false
print(sol.checkValidString("()()"))#true
print(sol.checkValidString("("))#false
print(sol.checkValidString(")"))#false
print(sol.checkValidString("(((******))"))#true
print(sol.checkValidString("(*))"))#true

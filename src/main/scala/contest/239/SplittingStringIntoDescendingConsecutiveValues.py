from math import inf
from collections import defaultdict

class Solution:
    def splitString(self, s: str) -> bool:
        if not s or len(s) < 2:
            return False

        def backtrack(c, last_num, count, mem):
            if c == len(s):
                return count >= 2
            if count > 1 and last_num - int(s[c:]) == 1:
                return True
            if (c,last_num, count) in mem:
                return mem[(c,last_num, count)]
            splited = False
            for i in range(c, len(s)):
                a = int(s[c:i + 1])
                if count == 0 or last_num - a == 1:
                    splited = backtrack(i + 1, a, count + 1, mem)
                    if splited:
                        break
            mem[(c, last_num, count)] = splited
            return splited

        mem = defaultdict(int)
        return backtrack(0, inf, 0, mem)


sol = Solution()
print(sol.splitString("9080701"))#false
print(sol.splitString("050043"))#true
print(sol.splitString("12"))#false

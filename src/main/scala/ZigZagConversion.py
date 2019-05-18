from collections import defaultdict

class Solution:
    def convert(self, s, numRows):
        if not s or not numRows:
            return s
        r = 0
        i = 0
        m = defaultdict(list)
        while i < len(s):
            while r < numRows and i < len(s):
                m[r].append(s[i])
                i += 1
                r += 1
            r -= 2
            while r > 0 and i < len(s):
                m[r].append(s[i])
                i += 1
                r -= 1
            r = 0
        res = ''
        for i in range(numRows):
            for j in range(len(m[i])):
                res += m[i][j]
        return res


sol = Solution()
print(sol.convert("PAYPALISHIRING", 4))


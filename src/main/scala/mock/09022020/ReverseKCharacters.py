class Solution:
    def reverseStr(self, s, k):
        if not s:
            return s
        i = 0
        res = ''
        while i < len(s):
            res += s[i:i + k][::-1]
            if i + k < len(s):
                res += s[i + k:i + 2 * k]
            i += 2 * k
        return res


sol = Solution()
print(sol.reverseStr(s = "abcdefg", k = 2))
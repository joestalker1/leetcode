class Solution:
    def reverseString(self, s):
        res = ' ' * len(s)
        i = len(s) - 1
        for ch in s:
            res[i] = ch
            i -= 1
        return res

sol = Solution()
print(sol.reverseString(""))
print(sol.reverseString("hello"))
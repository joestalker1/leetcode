class Solution:
    def findLUSlength(self, s1, s2):
        if s1 == s2:
            return -1
        return max(len(s1), len(s2))

sol = Solution()
print(sol.findLUSlength("a", "aaa"))
print(sol.findLUSlength("aefeaf", ""))
print(sol.findLUSlength("abc", "cdc"))


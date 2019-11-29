class Solution(object):
    def countSubstrings(self, s):
        if not s:
            return 0
        res = 0
        for center in range(2*len(s) - 1):
            left = center // 2
            right = left + center % 2
            while left >= 0 and right < len(s) and s[left] == s[right]:
                res += 1
                left -= 1
                right += 1
        return res


sol = Solution()
print(sol.countSubstrings("aaa"))
print(sol.countSubstrings("abc"))



class Solution:
    def countHomogenous(self, s):
        if not s:
            return 0
        l = 0
        res = 0
        mod = 10 ** 9 + 7
        for r in range(len(s)):
            if s[l] != s[r]:
                cur_len = r - l
                res = (res + cur_len * (cur_len + 1) // 2) % mod
                l = r
        # count last substring
        cur_len = r - l + 1
        res = (res + cur_len * (cur_len + 1) // 2) % mod
        return res


s = Solution()
print(s.countHomogenous("abbcccaa"))



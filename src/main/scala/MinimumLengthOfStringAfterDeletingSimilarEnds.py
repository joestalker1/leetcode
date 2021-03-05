class Solution:
    def minimumLength(self, s: str) -> int:
        l = 0
        r = len(s) - 1
        while l <= r and s[l] == s[r]:
            ch = s[l]
            while l <= r and ch == s[l]:
                l += 1
            while r >= l and ch == s[r]:
                r -= 1
        return r-l+1

sol = Solution()
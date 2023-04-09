class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        if k == 1:
            return len(s)
        
        def is_poly(s, l,r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True
        dp = [0] * len(s)
        dp[k-1] = 1 if is_poly(s,0,k-1) else 0
        for i in range(k, len(s)):
            dp[i] = dp[i-1]
            for j in range(i - k + 1):
                if is_poly(s, j, i):
                    print(s[j:i+1])
                    dp[i] += 1
        return dp[-1]


sol = Solution()
print(sol.maxPalindromes("fttfjofpnpfydwdwdnns",2))
class Solution:
    def repeatedSubstringPattern(self, s):
        if not s or len(s) < 2:
            return False
        if len(s) == 2:
            return s[0] == s[1]
        dp = [0] * len(s)
        j = 0
        for i in range(1, len(s)):
            j = dp[i-1]
            while j > 0 and s[i] != s[j]:
                j = dp[j-1]
            if s[i] == s[j]:
                j += 1
            dp[i] = j
        n = len(s)
        l = dp[n-1]
        return l != 0 and (n-l) != 0 and n % (n-l) == 0


sol = Solution()
print(sol.repeatedSubstringPattern("ababab"))#true
print(sol.repeatedSubstringPattern("aaaaa"))
print(sol.repeatedSubstringPattern("abaababaab"))#true
print(sol.repeatedSubstringPattern("aaac"))#false
print(sol.repeatedSubstringPattern("abcabcabcabc"))#true

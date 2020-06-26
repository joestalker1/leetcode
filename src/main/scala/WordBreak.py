class Solution:
    def wordBreak(self, s, wordDict):
        if not s or not wordDict:
            return False
        dp = [False] * (len(s) + 1)
        dp[0] = True
        words = set(wordDict)
        for i in range(1, len(s) + 1):
            for j in range(i):
                if dp[j] and s[j:i] in words:
                    dp[i] = True
                    break
        return dp[- 1]


sol = Solution()
print(sol.wordBreak(s="catsandog", wordDict=["cats", "dog", "sand", "and", "cat"]))
print(sol.wordBreak(s="applepenapple", wordDict=["apple", "pen"]))
print(sol.wordBreak(s="leetcode", wordDict=["leet", "code"]))

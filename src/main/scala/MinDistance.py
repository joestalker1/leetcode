class Solution:
    def minDistance(self, word1, word2):
        if not word1 and not word2 or word1 == word2:
            return 0
        if not word1:
            return len(word2)
        if not word2:
            return len(word1)
        dp = [0] * (len(word2) + 1)
        for i in range(len(word1) + 1):
            new_dp = [0] * (len(word2) + 1)
            for j in range(len(word2)+1):
                if i == 0 or j == 0:
                    #remove all chars in non-empty string
                    new_dp[j] = max(i,j)
                    continue
                if word1[i-1] == word2[j-1]:
                    #take previous strings
                    new_dp[j] = dp[j-1]
                    continue
                else:
                    #remove current i and j in word1,word2
                    new_dp[j] = 1 + min(dp[j], new_dp[j - 1])
            dp = new_dp
        return dp[-1]
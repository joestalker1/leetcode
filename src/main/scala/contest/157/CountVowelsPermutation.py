class Solution:
    def countVowelPermutation(self, n):
        if n == 0:
            return 0
        chars = ['a', 'e', 'i', 'o', 'u']
        moves = {0: [1], 1: [0, 2], 3: [2, 4], 4: [0], 2: [1, 0, 3, 4]}
        dp = [0] * len(chars)
        for i in range(len(dp)):
            dp[i] = [0] * (n + 1)

        for i in range(len(dp)):
            dp[i][1] = 1
        for j in range(2, len(dp[0])):
            for i in range(len(chars)):
                to_chars = moves[i]
                for char in to_chars:
                    dp[char][j] += dp[i][j-1]
        count = 0
        base = 10 ** 9 + 7
        for j in range(len(dp)):
            count += (dp[j][n] % base)
        return count % base


sol = Solution()
print(sol.countVowelPermutation(5))
print(sol.countVowelPermutation(2))
print(sol.countVowelPermutation(1))

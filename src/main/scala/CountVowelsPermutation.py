class Solution:
    def countVowelPermutation(self, n):
        if n == 0:
            return 0
        MOD = 10 ** 9 + 7
        chars = ['a', 'e', 'i', 'o', 'u']
        #a follow by e
        #e follow by a, i and so on
        adj_list = {0: [1], 1: [0, 2], 3: [2, 4], 4: [0], 2: [1, 0, 3, 4]}
        # n is string length
        dp = [[0] * (n + 1) for _ in range(len(chars))]

        for i in range(len(dp)):
            dp[i][1] = 1
        # aCountNew = eCount + iCount + uCount
        # eCountNew = aCount + iCount
        # iCountNew = eCount + oCount
        # oCountNew = iCount
        # uCountNew = iCount + oCount
        #for every string length
        for l in range(2, (n+1)):
            for i in range(len(chars)):
                for next_char in adj_list[i]:
                    dp[next_char][l] += dp[i][l - 1] % MOD
        count = 0
        for j in range(len(dp)):
            count += dp[j][n] % MOD
        return count % MOD
class Solution:
    def atMostNGivenDigitSet(self, digits, n: int) -> int:
        s = str(n)
        k = len(s)
        # store numbor of [i:n]
        dp = [0] * k + [1]
        for i in range(k-1,-1,-1):
            for d in digits:
                if s[i] > d:
                    #add count of s[i]xxxx - num of digits ** k-1
                    dp[i] += len(digits) ** (k-i-1)
                elif s[i] == d:
                    # it is only dxxx number
                    dp[i] += dp[i+1]
        return dp[0] + sum([len(digits) ** i for i in range(1,k)])


sol = Solution()
print(sol.atMostNGivenDigitSet(["3","4","5","6"], 64))
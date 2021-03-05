from math import ceil

class Solution:
    def consecutiveNumbersSum(self, N):
        upper_limit = ceil((2 * N + 0.25) ** 0.5 - 0.5) + 1
        count = 0
        for k in range(1, upper_limit):
            if (N - k*(k+1)//2) % k == 0:
                count += 1
        return count

sol = Solution()
#print(sol.consecutiveNumbersSum(858951))#16
print(sol.consecutiveNumbersSum(5))#2
print(sol.consecutiveNumbersSum(15))#4

print(sol.consecutiveNumbersSum(9))#3
print(sol.consecutiveNumbersSum(8))#1
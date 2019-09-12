from math import sqrt, factorial
class Solution:
    def numPrimeArrangements(self, n):
        if not n:
            return 0
        primes = [1] * (n + 1)
        primes[0] = 0
        primes[1] = 0

        for a in range(2, int(sqrt(n)) + 1):
            if primes[a] == 0:
                continue
            x = 2 * a
            while x <= n:
                primes[x] = 0
                x += a
        prime_num = sum(primes)
        composite_num = n - prime_num
        sol_num = factorial(prime_num)
        if composite_num > 0:
            sol_num *= factorial(composite_num)
        return sol_num % (10 ** 9 + 7)

sol = Solution()
print(sol.numPrimeArrangements(100))
print(sol.numPrimeArrangements(5))







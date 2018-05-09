import math
class Solution:
    def isUgly(self, num):
        if num <= 1:
            return num == 1
        primes = [True] * (num + 1)
        primes[0] = False
        primes[1] = False
        c = math.ceil(math.sqrt(num))
        good = set([2, 3, 5])
        for a in range(2, c + 1):
            if primes[a]:
                if num % a == 0:
                    if a not in good:
                        return False
                    b = num // a
                    if primes[b] and b not in good:
                        return False
                b = a * a
                while b <= c:
                    primes[b] = False
                    b += a
        return True


sol = Solution()
print(sol.isUgly(2))
print(sol.isUgly(7))
print(sol.isUgly(214797179))

class Solution:
    def maxNiceDivisors(self, primeFactors: int):

        def power(x,p, mod):
            res = 1
            while p:
                if p & 1 == 1:
                    res = (res * x) % mod
                p >>= 1
                x = (x * x) % mod
            return res

        if primeFactors <= 3:
            return primeFactors
        mod = 10 ** 9 + 7
        div3 = primeFactors // 3
        rem = primeFactors % 3
        if rem == 0:
            return power(3, div3, mod)
        if rem == 1:
            div3 -= 1
            rem = 4
            return (rem * power(3, div3, mod)) % mod
        return (rem * power(3,div3, mod)) % mod


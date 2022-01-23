class Solution:
    def nthMagicalNumber(self, n: int, a: int, b: int) -> int:
        MOD = 10 ** 9 + 7

        def gcd(a, b):
            if b == 0:
                return a
            return gcd(b, a % b)

        mul_of_ab = a * b // gcd(a, b)
        # count how many numbers we can get from 1 to mul_of_ab
        m = mul_of_ab // a + mul_of_ab // b - 1  # 1 is of number that is multiple of a and b
        # count many multiple we need to get n-th number
        q = n // m
        r = n % m
        res = q * mul_of_ab % MOD
        if r == 0:
            return res
        head = [a, b]
        res = q * mul_of_ab % MOD
        for i in range(r - 1):
            if head[0] <= head[1]:
                head[0] += a
            else:
                head[1] += b
        res += min(head)
        return res % MOD
    
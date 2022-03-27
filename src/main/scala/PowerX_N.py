class Solution:
    def myPow(self, x: float, n: int) -> float:

        def calc_power(x, n):
            if n == 0:
                return 1
            if n == 1:
                return x
            p = calc_power(x * x, n // 2)
            if n % 2 == 1:
                p *= x
            return p

        abs_x = abs(x)
        abs_n = abs(n)
        p = calc_power(abs_x, abs_n)
        p *= (-1 if x < 0 and abs_n % 2 != 0 else 1)
        if n < 0:
            return 1 / p
        return p

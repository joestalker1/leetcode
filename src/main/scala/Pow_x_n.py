class Solution:
   def myPow(self, x: float, n: int):
        def pow(x, n):
            if n == 0:
                return 1
            if n % 2 == 0:
                a = pow(x, n // 2)
                return a * a
            else:
                a = pow(x, (n - 1) // 2)
                return a * a * x
        if n < 0:
            n = - n
            x = 1 / x
        return pow(x, n)


sol = Solution()
print(sol.myPow(2.00000, -2))
#print(sol.myPow(2.00000, 10))
#print(sol.myPow(2.10000, 3))


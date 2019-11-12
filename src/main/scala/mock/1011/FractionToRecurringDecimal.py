class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        if denominator == 0:
            return Exception('denominator is 0')
        if numerator == 0:
            return '0'
        res = []
        if (denominator < 0) ^ (numerator < 0):
            res.append('-')
        a = abs(numerator)
        b = abs(denominator)
        res.append(str(a // b))
        a = a % b
        if a == 0:
            return ''.join(res)
        res.append('.')
        remainders = {}
        while a != 0:
            if a in remainders:
                p = remainders[a]
                res.insert(p, '(')
                res.append(')')
                break
            remainders[a] = len(res)
            a *= 10
            res.append(str(a // b))
            a = a % b
        return ''.join(res)



sol = Solution()
print(sol.fractionToDecimal(-50, 8))
print(sol.fractionToDecimal(0, 3))#0
print(sol.fractionToDecimal(1, 333))
print(sol.fractionToDecimal(1, 6))
print(sol.fractionToDecimal(4, 333))
print(sol.fractionToDecimal(numerator = 2, denominator = 3))
print(sol.fractionToDecimal(numerator = 2, denominator = 1))#2
print(sol.fractionToDecimal(numerator = 1, denominator = 2))#0.5












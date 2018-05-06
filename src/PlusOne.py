class Solution(object):
    def plusOne(self, digits):
        if not digits:
            return digit
        shift = 1
        res = []
        for i in range(len(digits) - 1,-1, -1):
            digit = digits[i]
            a = digit
            if shift:
                a += shift
            if a >= 10:
               digit = a % 10
               shift = a // 10
            else:
               digit = a
               shift = 0
            res.insert(0, digit)
        if shift:
            res.insert(0, shift)
        return res

sol = Solution()
print(sol.plusOne([9, 9]))
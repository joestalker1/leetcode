class Solution:
    def plusOne(self, digits):
        if not digits:
            return digits
        carry = 0
        res = []
        n = len(digits)
        for i in range(len(digits) - 1, -1, -1):
            if i == n - 1:
                a = digits[i] + 1
                res.append(a % 10)
                carry = a // 10
            else:
                a = digits[i] + carry
                res.append(a % 10)
                carry = a // 10
        if carry:
            res.append(carry)
        reversed(res)
        return res

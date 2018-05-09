class Solution:
    def addStrings(self, num1, num2):
        i = len(num1) - 1
        j = len(num2) - 1
        carry = 0
        res = ''
        while i >= 0 or j >= 0 or carry == 1:
            a = int(num1[i]) if i >= 0 else 0
            b = int(num2[j]) if j >= 0 else 0
            a = a + b + carry
            carry = a // 10
            res = str(a % 10) + res
            i -= 1
            j -= 1
        return res


sol = Solution()
print(sol.addStrings("99", "9"))
print(sol.addStrings("900", "100"))

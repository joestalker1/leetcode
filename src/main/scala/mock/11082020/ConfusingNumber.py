class Solution:
    def confusingNumber(self, N: int):
        a = N
        digits = []
        while a > 0:
            digits.append(a % 10)
            a = a // 10
        i = 0
        j = len(digits) - 1
        while i < j:
            if digits[i] == digits[j] and digits[i] in [0,1,8] or digits[i] == 6 and digits[j] == 9 or  digits[i] == 9 and digits[j] == 6:
                i += 1
                j -= 1
            else:
                return False
        return digits[i] in [0,1,8] if len(digits) % 2 == 1 else True


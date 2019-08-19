class Solution:
    def sumOfDigits(self, A):
        if not A:
            return 0
        min_val = min(A)
        sum_of_digits = 0
        while min_val:
            digit = min_val % 10
            min_val = min_val // 10
            sum_of_digits += digit
        return 1 if sum_of_digits % 2 == 0 else 0


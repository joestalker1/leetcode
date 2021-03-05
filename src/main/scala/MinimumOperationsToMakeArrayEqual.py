class Solution:
    def minOperations(self, n):
        if n <= 1:
            return 0
        diff_sum = 0
        # (n  - i) where i is odd is number needs to add/subtract.
        # find sum (n-1) + (n - 3) + (n-5)
        while n > 0:
            diff_sum += n - 1
            # calculate the next number
            n -= 2
        return diff_sum


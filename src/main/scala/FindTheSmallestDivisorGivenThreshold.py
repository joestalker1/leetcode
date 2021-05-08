import math

class Solution:
    def smallestDivisor(self, nums, threshold) -> int:
        lo = 1
        hi = 10 ** 6

        def canDivide(d):
            sum_of_div = 0
            for a in nums:
                sum_of_div += math.ceil(a / d)
                if sum_of_div > threshold:
                    return False
            return True

        while lo < hi:
            m = lo + (hi - lo) // 2
            if canDivide(m):
                hi = m
            else:
                lo = m + 1
        return lo


sol = Solution()
print(sol.smallestDivisor([1,2,5,9] ,6))#5
import bisect
import math
class Solution:
   # fast way to generate subset sums
    def generateSubsetSums(self, nums):
            # 0 gives to add tne items as sums
            ans = {0}
            for x in nums:
                ans |= {x + y for y in ans}
            return ans

    def minAbsDifference(self, arr, target):
        # divide arr by 2 and generate sum for left and right parts
        n = len(arr)
        left = sorted(self.generateSubsetSums(arr[:n // 2]))
        right = self.generateSubsetSums(arr[n // 2:])
        # max sum is less then target
        res = math.inf
        for s in right:
            # return x[:k] < target - s and x[k:] >= target -s
            k = bisect.bisect_left(left, target - s)
            # consider two cases:
            if k < len(left):
                res = min(res, s + left[k] - target)
            if k > 0:
                res = min(res, target - s - left[k-1])
        return res


sol = Solution()
print(sol.minAbsDifference([5,-7,3,5], 6))



class Solution:
    def maxSubArray(self, nums):
        # assert self._maxSubArray([1,1,1]) == 3,'all positive num'
        # assert self._maxSubArray([-10,1,-20]) == 1,'all positive num'
        # assert self._maxSubArray([1]) == 1,'one number'
        return self._maxSubArray(nums)

    def _maxSubArray(self, nums):
        max_sum = -inf
        cur_max = 0
        for i in range(len(nums)):
            # pickup either: current item or cur_max + current item
            cur_max = max(nums[i], cur_max + nums[i])
            max_sum = max(max_sum, cur_max)
        return max_sum

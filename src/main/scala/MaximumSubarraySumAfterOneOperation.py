import math

class Solution:
    def maxSumAfterOperation(self, nums):
        #max subarray length without double item
        cur_sum1 = 0
        # max subarray length with double item
        cur_sum2 = 0
        #global max subarray length
        max_sum = -math.inf
        for i in range(len(nums)):
            # max len either current item, or previous subarray + current item
            new_cur_sum1 = max(nums[i], cur_sum1 + nums[i])
            #max len either current item ^2 or subarray with previous double item or prevoius subarray(without item doubling) + double current item
            new_cur_sum2 = max(nums[i] * nums[i], cur_sum2 + nums[i],cur_sum1 + nums[i] * nums[i])
            # pick up the max subarray length
            max_sum = max(max_sum, new_cur_sum1, new_cur_sum2)
            # update my variables
            cur_sum1 = new_cur_sum1
            cur_sum2 = new_cur_sum2
        return max_sum
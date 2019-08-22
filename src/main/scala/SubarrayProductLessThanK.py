class Solution:
    def numSubarrayProductLessThanK(self, nums, k):
        if not nums or k <= 0:
            return 0
        s = -1
        e = -1
        sub_arr_sum = 0
        sub_arr_count = 0
        for i in range(len(nums)):
            if s == -1:
                sub_arr_sum = 

        return sub_arr_count

class Solution:
    def minOperations(self, nums, x):
        total = sum(nums)
        if total == x:
            return len(nums)
        max_len = -1
        #find max subsequence equal to total - x
        need_sum = total - x
        left = 0
        cur_sum = 0
        right = 0
        while right < len(nums):
            cur_sum += nums[right]
            while cur_sum >= need_sum and left <= right:
                if cur_sum == need_sum:
                    max_len = max(max_len, right - left + 1)
                cur_sum -= nums[left]
                left += 1
            right += 1
        return len(nums) - max_len if max_len != -1 else -1


sol = Solution()
print(sol.minOperations([],0))
print(sol.minOperations([1,1], 3))#3
print(sol.minOperations([8828,9581,49,9818,9974,9869,9991,10000,10000,10000,9999,9993,9904,8819,1231,6309], 134365))#16








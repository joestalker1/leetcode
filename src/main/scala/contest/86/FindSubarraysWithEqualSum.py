class Solution:
    def findSubarrays(self, nums) -> bool:
        if len(nums) < 3:
            return False
        sum_to_pos = set()
        for i in range(len(nums) - 1):
            cur_sum = nums[i] + nums[i+1]
            if cur_sum in sum_to_pos:
                return True
            sum_to_pos.add(cur_sum)
        return False

sol = Solution()
print(sol.findSubarrays([1,2,3,4,5]))#False
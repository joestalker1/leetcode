class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        if not nums:
            return 0

        # if i can split array by <= m parts
        def can_split(max_sum):
            count = 1
            cur_sum = 0
            for i in range(len(nums)):
                if cur_sum + nums[i] <= max_sum:
                    cur_sum += nums[i]
                else:
                    cur_sum = nums[i]
                    count += 1
            return count <= m

        lo = max(nums)
        hi = sum(nums) + 1
        while lo < hi:
            max_sum = lo + (hi - lo) // 2
            # if it can split,so try to take lesser max_sum
            if can_split(max_sum):
                hi = max_sum
            else:
                lo = max_sum + 1
        return lo



sol = Solution()
print(sol.splitArray([10,5,13,4,8,4,5,11,14,9,16,10,20,8], 8))#25
print(sol.splitArray([1,2147483646], 1))#1
print(sol.splitArray([2,3,1,2,4,3], 5))#4
print(sol.splitArray([7,2,5,10,8], 2))#18


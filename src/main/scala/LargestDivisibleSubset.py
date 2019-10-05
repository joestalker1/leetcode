class Solution:
    def largestDivisibleSubset(self, nums):
        if not nums:
            return []
        nums.sort()
        dp = [1] * len(nums)
        for i in range(1, len(nums)):
            for j in range(0, i):
                if nums[i] % nums[j] == 0:
                    dp[i] = max(dp[i], dp[j] + 1)
        #look up max by first item in tuple
        max_len,max_index = max([(v, i) for i,v in enumerate(dp)])
        cur_tail,cur_size = nums[max_index],max_len
        res = []
        for i in range(max_index, -1, -1):
            if dp[i] == cur_size and cur_tail % nums[i] == 0:
                res.insert(0, nums[i])
                cur_size -= 1
                cur_tail = nums[i]
        return res




sol = Solution()
print(sol.largestDivisibleSubset([2,3,4,9,8]))#[2,4,8]
print(sol.largestDivisibleSubset([4,8,10,240]))
print(sol.largestDivisibleSubset([1,2,3]))
print(sol.largestDivisibleSubset([1]))
print(sol.largestDivisibleSubset([1,2,4,8]))
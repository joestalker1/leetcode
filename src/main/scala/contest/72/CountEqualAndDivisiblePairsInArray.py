class Solution:
    def countPairs(self, nums, k) -> int:
        cnt = 0
        for i in range(len(nums) - 1):
            for j in range(i+1, len(nums)):
                if nums[i] == nums[j] and (i * j) % k == 0:
                    cnt += 1
        return cnt


sol = Solution()
print(sol.countPairs([3,1,2,2,2,1,3],2))#4
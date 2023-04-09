from collections import defaultdict

class Solution:
    def xorBeauty(self, nums) -> int:
        freq = defaultdict(int)
        nums = list(set(nums))
        for i in range(len(nums)):
            for j in range(len(nums)):
                freq[nums[i] | nums[j]] += 1
        new_freq = {k:v for k,v in freq.items() if freq[k] % 2 != 0}
        res = 0
        for num in nums:
            for k in new_freq:
                res ^= k & num
        return res


sol = Solution()
print(sol.xorBeauty([1,4]))#5

#1,3,3,1 for 1,4
# 1,4,12,8 for 1,4,4
#[[1, 1, 1], [1, 1, 4], [1, 4, 4], [4, 4, 4]]
# 0 - 1, last is 1, other is 3
#[[1, 1, 1], [1, 1, 4], [1, 1, 4], [1, 4, 1], [1, 4, 4], [1, 4, 4], [1, 4, 1], [1, 4, 4], [1, 4, 4], [4, 1, 1], [4, 1, 4], [4, 1, 4], [4, 4, 1], [4, 4, 4], [4, 4, 4], [4, 4, 1], [4, 4, 4], [4, 4, 4], [4, 1, 1], [4, 1, 4], [4, 1, 4], [4, 4, 1], [4, 4, 4], [4, 4, 4], [4, 4, 1], [4, 4, 4], [4, 4, 4]]
#[[1, 1, 1], [1, 1, 4], [1, 4, 1], [1, 4, 4], [4, 1, 1], [4, 1, 4], [4, 4, 1], [4, 4, 4]]
print(sol.xorBeauty([15,45,20,2,34,35,5,44,32,30])) #34
from math import inf

class Solution:
    def buildArray(self, nums):

        def find_val():
            for i in range(len(nums)):
                if i != nums[i] and nums[i] > 0:
                    return i

        j = find_val()
        nxt = nums[j]
        for _ in range(len(nums)):
            if nums[nxt] == 0:
                nums[j] = -inf
            else:
                nums[j] = -nums[nxt]
            j = nxt
            if nums[j] == j or nums[j] < 0:
                j = find_val()
            nxt = nums[j]
        for i in range(len(nums)):
            if nums[i] == -inf:
                nums[i] = 0
            else:
                nums[i] = -nums[i]
        return nums


sol = Solution()
print(sol.buildArray([0,2,1,5,3,4]))#[0,1,2,4,5,3]

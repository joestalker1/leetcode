class Solution(object):
    def findMaxLength(self, nums):
        if not nums:
            return 0
        m = {0: -1}
        count = 0
        max_len = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                count += -1
            else:
                count += 1
            if count in m:
                max_len = max(max_len, i - m[count])
            else:
                m[count] = i

        return max_len


sol = Solution()
print(sol.findMaxLength([0,1,0,1,1,1,0,0,1,1,0,1,1,1,1,1,1,0,1,1,0,1,1,0,0,0,1,0,1,0,0,1,0,1,1,1,1,1,1,0,0,0,0,1,0,0,0,1,1,1,0,1,0,0,1,1,1,1,1,0,0,1,1,1,1,0,0,1,0,1,1,0,0,0,0,0,0,1,0,1,0,1,1,0,0,1,1,0,1,1,1,1,0,1,1,0,0,0,1,1]))#68
print(sol.findMaxLength( [0,1,0]))
print(sol.findMaxLength([0,1]))



class Solution:
    def maxResult(self, nums, k):
        n = len(nums)
        res = nums[0]
        dq = [[0,nums[0]]]
        for i in range(1, n):
            while dq and dq[0][0] < (i - k):
                dq.pop(0)
            res = nums[i] + dq[0][1]
            while dq and dq[-1][1] <= res:
                dq.pop()
            dq.append([i,res])
        return res



sol = Solution()
print(sol.maxResult([1,-1,-2,4,-7,3], 2))
print(sol.maxResult([1,2,3], 1))


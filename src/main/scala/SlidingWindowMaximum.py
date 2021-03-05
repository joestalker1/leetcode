class Solution:
    def maxSlidingWindow(self, nums, k):
        n = len(nums)
        dq = []
        res = []
        for i in range(n):
            while dq and dq[0][0] <= i - k:
                dq.pop(0)
            while dq and dq[-1][1] <= nums[i]:
                dq.pop()
            dq.append([i, nums[i]])
            if i + 1 >= k:
                res.append(dq[0][1])
        return res


sol = Solution()
print(sol.maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3))#[3,3,3,5,5,6,7]
print(sol.maxSlidingWindow([1,3,-1,-3,5,3,6,7], 2))#[3,3,-1,5,5,6,7]



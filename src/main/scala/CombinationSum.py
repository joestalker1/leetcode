class Solution:
    def combinationSum(self, nums, target):
        if not nums:
            return []

        def get_comb_sum(start,res, buf, rem):
            if rem == 0:
                res.append(buf[::])
                return
            if rem < 0:
                return
            for i in range(start, len(nums)):
                buf.append(nums[i])
                get_comb_sum(i+1,res,buf,rem - nums[i])
                buf.pop()
        res = []
        get_comb_sum(0, res, [], target)
        return res


sol = Solution()
print(sol.combinationSum([2,3,5, 4,4], 8))
#print(sol.combinationSum([2,3,6,7], 7))
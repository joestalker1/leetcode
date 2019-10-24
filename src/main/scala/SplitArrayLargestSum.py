class Solution:
    def splitArray(self, nums, m):
        if not nums or m == 0:
            return 0
        lo = 0
        hi = 0
        for i in range(len(nums)):
            hi += nums[i]
            if nums[i] > lo:
                lo = nums[i]
        res = hi
        while lo <= hi:
            f = lo + (hi - lo) // 2
            sum_nums = 0
            cnt = 1
            for i in range(len(nums)):
                if sum_nums + nums[i] > f:
                    cnt += 1
                    sum_nums = nums[i]
                else:
                    sum_nums += nums[i]
            if cnt <= m:
                res = min(res, f)
                hi = f - 1
            else:
                lo = f + 1
        return res



sol = Solution()
print(sol.splitArray([10,5,13,4,8,4,5,11,14,9,16,10,20,8], 8))#25
print(sol.splitArray([1,2147483646], 1))#1
print(sol.splitArray([2,3,1,2,4,3], 5))#4
print(sol.splitArray([7,2,5,10,8], 2))#18


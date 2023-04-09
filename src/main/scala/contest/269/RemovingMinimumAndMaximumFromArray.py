class Solution:
    def minimumDeletions(self, nums) -> int:
        if len(nums) < 3:
            return len(nums)
        min_val = min(nums)
        min_i = nums.index(min_val)
        max_val = max(nums)
        max_i = nums.index(max_val)
        n = len(nums)
        mi = min(min_i,max_i)
        mai = max(min_i, max_i)
        min_i = mi
        max_i = mai
        a = min_i+1 + n - max_i
        b = max_i + 1
        c = n-min_i
        return min(a,b,c)


sol = Solution()
print(sol.minimumDeletions([2,10,7,5,4,1,8,6]))
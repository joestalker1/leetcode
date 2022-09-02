class Solution:
    def zeroFilledSubarray(self, nums) -> int:
        if not nums:
            return 0
        l = 0
        cnt = 0
        for r in range(len(nums)):
            if nums[r] != 0:
                cur_len = r - l
                cnt += cur_len*(cur_len+1)//2
                l = r + 1
        if nums[-1] == 0:
            cur_len = r - l + 1
            cnt += cur_len* (cur_len+1) // 2
        return cnt


sol = Solution()
print(sol.zeroFilledSubarray([1,3,0,0,2,0,0,4]))#6
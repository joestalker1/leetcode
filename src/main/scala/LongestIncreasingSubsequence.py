import bisect

class Solution:
    def lengthOfLIS(self, nums):
        if not nums:
            return 0
        tail = [0 for i in range(len(nums) + 1)]
        cur_len = 1
        tail[0] = nums[0]
        for i in range(1, len(nums)):
            #if end of max sequence is less than last item of most length sequence, let update with nums[i]
            if nums[i] > tail[cur_len-1]:
                tail[cur_len] = nums[i]
                cur_len += 1
            else:
                #find max len sequence with end item being less nums[i] to replace it.
                j = bisect.bisect_left(tail,nums[i], 0, cur_len)
                tail[j] = nums[i]
        return cur_len


sol = Solution()
print(sol.lengthOfLIS([4,10,4,3,8,9]))#3

print(sol.lengthOfLIS([10,9,2,5,3,4]))#3
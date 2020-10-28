class Solution:
    def isPossible(self, nums):
        if not nums:
            return []
        n = len(nums)
        used = set()
        while n > 0:

            seq_len = 0
            last_added = None
            for i in range(len(nums)):
                if i in used:
                    continue
                if not last_added or last_added + 1 == nums[i]:
                    last_added = nums[i]
                    seq_len += 1
                    used.add(i)
                if seq_len >= 3 and n - seq_len == 3:
                    break
            if seq_len < 3:
                return False
            n -= seq_len
        return len(used) == len(nums)


sol = Solution()
print(sol.isPossible([4,5,6,7,7,8,8,9,10,11])) # true
print(sol.isPossible([1,2,5,5,6,6,7,8,8,9])) # false

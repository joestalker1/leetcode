class Solution:
    def minKBitFlips(self, nums, k: int) -> int:
        q = []
        flips = 0
        for i in range(len(nums)):
            if q and q[0] <= i-k:
                q.pop(0)
            if len(q) % 2 == nums[i]:
                if i + k > len(nums):
                    return -1
                flips += 1
                q.append(i)
        return flips
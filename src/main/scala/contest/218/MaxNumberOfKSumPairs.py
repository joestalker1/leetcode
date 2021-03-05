class Solution:
    def maxOperations(self, nums, k):
        prev = {}
        res = 0
        for a in nums:
            r = k - a
            if r in prev:
                prev[r] -= 1
                if prev[r] == 0:
                    del prev[r]
                res += 1
            else:
                prev[a] += 1
        return res

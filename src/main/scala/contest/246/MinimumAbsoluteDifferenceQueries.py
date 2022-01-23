from math import *

class Solution:
    def minDifference(self, nums, queries):
        # assert self._minDifference([1],[[0,0]]) == [-1], 'test1'
        # assert self._minDifference([1,2],[[0,1]]) == [1], 'test2'
        # assert self._minDifference([1,2,4],[[0,2]]) == [1], 'test3'
        return self._minDifference(nums, queries)

    def _minDifference(self, nums, queries):
        freq = [[0] * 101 for _ in range(len(nums) + 1)]
        # count frequency of numbers from 1 to 10 for subarrays [1..i]
        for i in range(len(nums)):
            for a in range(1, 101):
                freq[i + 1][a] += freq[i][a]
            freq[i + 1][nums[i]] += 1
        ans = [-1] * len(queries)
        cnt = [0] * 101
        for k, query in enumerate(queries):
            i, j = query
            # count of frequency of 1 .. 100 for subarray [i:j+1]
            for a in range(0, 101):
                cnt[a] = freq[j + 1][a] - freq[i][a]
            prev = -1
            max_abs_val = inf
            # calculate difference between neighboring numbers
            for a in range(1, 101):
                if cnt[a] == 0:
                    continue
                if prev != - 1 and (a - prev) < max_abs_val:
                    max_abs_val = a - prev
                prev = a
            if max_abs_val != inf:
                ans[k] = max_abs_val
        return ans


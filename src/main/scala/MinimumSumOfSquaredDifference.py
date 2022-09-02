from collections import Counter

class Solution:
    def minSumSquareDiff(self, nums1, nums2, k1: int, k2: int) -> int:
        # assert self._minSumSquareDiff([],[],0,0) == 0,'test1'
        # assert self._minSumSquareDiff([1],[],0,0) == 0,'test2'
        # assert self._minSumSquareDiff([],[2],0,0) == 0,'test3'
        # assert self._minSumSquareDiff([3,1],[1,3],1,1) == 2,'test4'
        # assert self._minSumSquareDiff([1,2,2],[1,2,2],2,2) == 3,'test5'
        return self._minSumSquareDiff(nums1, nums2, k1, k2)

    def _minSumSquareDiff(self, nums1, nums2, k1: int, k2: int) -> int:
        if not nums1 or not nums2:
            return 0
        diff_arr = [abs(nums1[i] - nums2[i]) for i in range(len(nums1))]
        max_val = max(diff_arr)
        # count of value frequency
        freq = Counter(diff_arr)
        k = k1 + k2
        # for every value decrease its frequency(every val's decreased by 1) and increasing frequency of i- 1 item
        for i in range(max_val + 1, 0, -1):
            if freq[i] == 0:
                continue
            # how many items we can decrease.
            cnt = min(k, freq[i])
            freq[i] -= cnt
            # increase frequency of i - 1 items
            freq[i - 1] += cnt
            # subtract used number of item.
            k -= cnt
        squared_sum = 0
        # count of number squered item.
        for i in range(max_val + 1, 0, -1):
            if freq[i] > 0:
                squared_sum += freq[i] * i * i
        return squared_sum
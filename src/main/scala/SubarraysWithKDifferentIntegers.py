from collections import defaultdict


class Solution:
    def subarraysWithKDistinct(self, A, K):
        if not A or K == 0:
            return 0
        return self._subArraysWithKDistinct(A, K) - self._subArraysWithKDistinct(A, K - 1)

    def _subArraysWithKDistinct(self, A, K):
        l = 0
        num_to_count = defaultdict(int)
        res = 0
        for r in range(len(A)):
            num_to_count[A[r]] += 1
            while K < len(num_to_count.keys()):
                num_to_count[A[l]] -= 1
                if num_to_count[A[l]] == 0:
                    del num_to_count[A[l]]
                l += 1
            res += r - l + 1
        return res


sol = Solution()
print(sol.subarraysWithKDistinct([2, 1, 1, 1, 2], 1))  # 8
print(sol.subarraysWithKDistinct(A=[1, 2, 1, 3, 4], K=3))  # 3
print(sol.subarraysWithKDistinct(A=[1, 2, 1, 2, 3], K=2))  # 7

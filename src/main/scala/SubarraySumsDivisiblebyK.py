from collections import Counter

class Solution:
    def subarraysDivByK(self, arr, k):
        if not arr or len(arr) == 0 or k == 0:
            return 0
        p = [0]
        for x in arr:
            p.append((p[-1] + x) % k)

        freq = Counter(p)
        return int(sum(v * (v - 1) // 2 for v in freq.values()))


sol = Solution()
print(sol.subarraysDivByK([1, -10, 5], 9))
print(sol.subarraysDivByK([-5], 5))
print(sol.subarraysDivByK([4, 5, 0, -2, -3, 1], 5))

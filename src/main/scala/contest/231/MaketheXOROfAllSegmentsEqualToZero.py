from collections import Counter

class Solution:
    def minChanges(self, nums, k: int):
        if not nums or k == 0:
            return 0
        n = len(nums)
        groups = n // k
        n = k * groups
        cnt = 0
        freq = Counter(nums[:n])
        if k == 1:
            return n - freq.get(0, 0)
        sorted_arr = sorted(freq.keys(), key=lambda x: freq[x], reverse=True)
        cand = []
        for i in range(k):
            cand.append(sorted_arr[i])
            cnt += (groups - freq[sorted_arr[i]])

        if groups % 2 == 1:
            # needs to have one group results in 0
            x = 0
            for a in cand:
                x ^= a
            if x != 0:
                num_with_min_freq = min(cand, key=lambda x: freq[x])
                cnt = cnt - (groups - freq[num_with_min_freq]) + k
        return cnt


sol = Solution()
print(sol.minChanges([26,19,19,28,13,14,6,25,28,19,0,15,25,11],3))#11
print(sol.minChanges([23,27,14,0,14,3,7,10,14,23,5,5], 1))#11
print(sol.minChanges([6,1,7,2,1,7,3,4,7], 3))#3

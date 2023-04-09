from collections import Counter

class Solution:
    def makeSubKSumEqual(self, arr, k: int) -> int:
        if len(arr) == k:
            return 0
        n = len(arr)
        pr = [0] * (n + 1)
        for i in range(n):
            pr[i + 1] = pr[i] + arr[i]
        cur_sum = pr[k]
        eq_sum = True
        for i in range(k, n):
            if pr[i + 1] - pr[i + 1 - k] != cur_sum:
                eq_sum = False
                break
        if eq_sum:
            return 0
        min_op = 0
        if n // k < 2:
            freq = Counter(arr[:k])
            max_freq = 1
            need_item = 0
            for k in freq:
                if freq[k] > max_freq:
                    max_freq = freq[k]
                    need_item = k
            if max_freq > 1:
                for a in arr:
                    min_op += abs(a - need_item)
            else:
                sarr = sorted(arr[:k])
                if len(sarr) % 2 != 0:
                    need_item = sarr[len(sarr) / 2]
                else:
                    need_item = (sarr[len(sarr) / 2] + sarr[len(sarr) / 2 - 1]) // 2
                for a in arr:
                    min_op += abs(a - need_item)

        else:
            for i in range(k):
                sub_arr = []
                for j in range(i, n, k):
                    sub_arr.append(arr[j])
                sub_arr.sort()
                if len(sub_arr) % 2 != 0:
                    need_item = sub_arr[len(sub_arr) // 2]
                else:
                    need_item = (sub_arr[len(sub_arr) // 2] + sub_arr[len(sub_arr) // 2 - 1]) // 2
                for a in sub_arr:
                    min_op += abs(a - need_item)
        return min_op


sol = Solution()
print(sol.makeSubKSumEqual([2,10,9],1))#8




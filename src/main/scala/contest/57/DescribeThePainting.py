from collections import defaultdict

class Solution:
    def splitPainting(self, segments):
        #sum offset
        sums = defaultdict(int)
        # point where segment is starting/ending
        end = defaultdict(int)
        for s,e,c in segments:
            sums[s] += c
            sums[e] -= c
            end[s] = True
            end[e] = True
        res = []
        r = max(sums)
        cur_sum = 0
        last_i = 0
        for i in range(1, r + 1):
            if cur_sum > 0 and end[i] > 0:
                res.append([last_i,i,cur_sum])
            if end[i] > 0:
                last_i = i
            cur_sum += sums[i]
        return res


sol = Solution()
print(sol.splitPainting([[1,4,5],[4,7,7],[1,7,9]]))

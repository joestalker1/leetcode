class Solution:
    def maxValue(self, events, k):

        def find(lst, x):
            lo = 0
            hi = len(lst)
            while lo < hi:
                mid = lo + (hi - lo) // 2
                if x >= lst[mid][0]:
                    lo = mid + 1
                else:
                    hi = mid
            return lo

        def calc_value(lst, prev_end, rest, mem):
            if (prev_end, rest) in mem:
                return mem[(prev_end, rest)]
            if rest == 0:
                return 0
            max_val = 0
            s = find(lst, prev_end)
            for i in range(s, len(lst)):
                val1 = lst[i][2] + calc_value(lst, lst[i][1], rest - 1, mem)
                max_val = max(max_val, val1)
            mem[(prev_end, rest)] = max_val
            return max_val

        # N log N
        sorted_by_start = sorted(events, key=lambda x: x[0])
        return calc_value(sorted_by_start, -1, k, {})
class Solution:
    def merge(self, intervals):
        if not intervals:
            return intervals
        intervals.sort(key=lambda x: x[0])
        res = []
        for interval in intervals:
            #merge with last in res
            if not res or res[-1][1] < interval[0]:
                res.append(interval)
            elif res[-1][1] >= intervals[0]:
                res[-1][1] = max(res[-1][1], interval[1])
        return res

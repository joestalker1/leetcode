class Solution:
    def insert(self, intervals, newInterval):
        if not intervals:
            return [newInterval]
        if not newInterval:
            return intervals

        res = []
        new_s, new_e = newInterval
        i = 0
        # add intervals which start < newIntervals start
        while i < len(intervals) and intervals[i][0] < new_s:
            res.append(intervals[i])
            i += 1
        # may merge added intervals with newIntervals
        if not res or res[-1][1] < new_s:
            res.append(newInterval)
        else:
            res[-1][1] = max(new_e, res[-1][1])
        # add the rest of intervals if they overlap, let merge them
        while i < len(intervals):
            s, e = intervals[i]
            if res[-1][1] >= s:
                res[-1][1] = max(res[-1][1], e)
            else:
                res.append(intervals[i])
            i += 1
        return res




import bisect


class Solution:
    def minGroups(self, intervals) -> int:
        if not intervals:
            return 0

        res = []
        intervals.sort()
        for i in range(len(intervals)):
            if not res:
                res.append(intervals[i][1])
            else:
                j = bisect.bisect_right(res, intervals[i][0])
                if 0 <= j < len(res) and res[j] < intervals[i][0]:
                    res[j] = max(res[j], intervals[i][1])
                else:
                    res.insert(j,intervals[i][1])
        need_grp = len(intervals) - len(res)
        return need_grp if need_grp > 0 else 1


sol = Solution()
#print(sol.minGroups([[1,3],[5,6],[8,10],[11,13]]))#1
print(sol.minGroups([[5,10],[6,8],[1,5],[2,3],[1,10]]))#3






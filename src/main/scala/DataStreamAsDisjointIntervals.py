from sortedcontainers import SortedList

class SummaryRanges:
    def __init__(self):
        self.intervals = SortedList()

    def addNum(self, value: int) -> None:
        if not self.intervals:
            self.intervals.add(value)
        else:
            i = self.intervals.bisect_right(value)
            if i > 0 and self.intervals[i - 1] == value:
                return
            self.intervals.add(value)

    def getIntervals(self) -> List[List[int]]:
        if not self.intervals:
            return []
        l = -1
        r = -1
        res = []
        for v in self.intervals:
            if l == -1:
                l = r = v
            elif v == r + 1:
                r = v
            else:
                res.append([l, r])
                l = r = v
        res.append([l, r])
        return res
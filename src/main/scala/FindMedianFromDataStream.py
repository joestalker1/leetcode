from heapq import heappop,heappush

class MedianFinder:
    def __init__(self):
        self.lmax = [] # contain by 1 more items
        self.rmin = []

    def addNum(self, num: int) -> None:
        if not self.lmax or num <= -self.lmax[0]:
            heappush(self.lmax, -num)
        else:
            heappush(self.rmin, num)
        #balance 2 heaps
        if len(self.lmax) > len(self.rmin) + 1: # lmax > rmin + 1
            heappush(self.rmin, -heappop(self.lmax))
        elif len(self.lmax) < len(self.rmin):
            heappush(self.lmax, -heappop(self.rmin))

    def findMedian(self) -> float:
        L = len(self.lmax)
        R = len(self.rmin)
        if (L+R) % 2 == 0:
            return (-self.lmax[0] + self.rmin[0]) / 2
        return -self.lmax[0]


mf = MedianFinder()
mf.addNum(1)
mf.addNum(2)
print(mf.findMedian())
mf.addNum(3)
print(mf.findMedian())


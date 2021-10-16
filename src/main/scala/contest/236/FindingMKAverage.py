from heapq import heappop, heappush

class MKAverage:

    def __init__(self, m: int, k: int):
        self.lst = []
        self.m = m
        self.k = k
        self.min_items = []
        self.max_items = []

    def addElement(self, num: int) -> None:
        if len(self.min_items) < self.k:
            heappush(self.min_items, -num)
        elif len(self.max_items) < self.k:
            if -self.min_items[0] > num:
                a = -heappop(self.min_items)
                heappush(self.min_items, -num)
                heappush(self.max_items, a)
            else:
                heappush(self.max_items, num)
        else:
            if -self.min_items[0] > num:
                a = -heappop(self.min_items)
                heappush(self.min_items, -num)
                if len(self.min_items) + len(self.max_items) + len(self.lst) == self.m:
                    self.lst.pop(0)
                self.lst.append(a)
            else:
                if num > self.max_items[0]:
                    a = self.max_items[0]
                    heappop(self.max_items)
                    heappush(self.max_items, num)
                    if len(self.min_items) + len(self.max_items) + len(self.lst) == self.m:
                        self.lst.pop(0)
                    self.lst.append(a)
                else:
                    if len(self.min_items) + len(self.max_items) + len(self.lst) == self.m:
                        self.lst.pop(0)
                    self.lst.append(num)

    def calculateMKAverage(self) -> int:
        if len(self.lst) + len(self.min_items) + len(self.max_items) < self.m:
            return -1
        return sum(self.lst) // len(self.lst)
["MKAverage","addElement","addElement","calculateMKAverage","addElement","addElement","calculateMKAverage","addElement","addElement","calculateMKAverage","addElement"]
[[3,1],[17612],[74607],[],[8272],[33433],[],[15456],[64938],[],[99741]]
sol = MKAverage(3,1)
sol.addElement(17612)
sol.addElement(74607)
print(sol.calculateMKAverage())#-1
sol.addElement(8272)
sol.addElement(33433)
print(sol.calculateMKAverage())#33433
sol.addElement(15456)
sol.addElement(64938)
print(sol.calculateMKAverage())#33433
sol.addElement(99741)

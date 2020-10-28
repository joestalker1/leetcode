from heapq import heappop,heappush
from collections import defaultdict

from heapq import heappop, heappush
from collections import defaultdict


class Solution:
    def openLock(self, deadends, target):
        dead = set(deadends)
        q = [[0, '0000']]
        moves = defaultdict(lambda: float('inf'))
        while q:
            m, l = heappop(q)
            if l == target:
                return m
            w = [int(ch) for ch in l]
            for d1, d2, d3, d4 in [[0, 0, 0, 1], [0, 0, 1, 0], [0, 1, 0, 0], [1, 0, 0, 0], [0, 0, 0, -1], [0, 0, -1, 0],
                                   [0, -1, 0, 0], [-1, 0, 0, 0]]:
                w1 = w[0] + d1
                if w1 > 9:
                    w1 = 0
                if w1 < 0:
                    w1 = 9
                w2 = w[1] + d2
                if w2 > 9:
                    w2 = 0
                if w2 < 0:
                    w2 = 9
                w3 = w[2] + d3
                if w3 > 9:
                    w3 = 0
                if w3 < 0:
                    w3 = 9
                w4 = w[3] + d4

                if w4 > 9:
                    w4 = 0
                if w4 < 0:
                    w4 = 9
                new_l = str(w1) + str(w2) + str(w3) + str(w4)
                if new_l in dead:
                    continue
                if moves[new_l] > m + 1:
                    heappush(q, [m + 1, new_l])
                    moves[new_l] = m + 1
        return -1


sol = Solution()
print(sol.openLock(["0201","0101","0102","1212","2002"], "0202"))
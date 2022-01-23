from collections import defaultdict

#eulerian circuit
def hierholzer(adj):
    edge_count = defaultdict(lambda : 0)
    for i in range(len(adj)):
        edge_count[i] = len(adj[i])

    if not len(adj):
        return
    circuit = []
    curr_path = []
    curr_path.append(0)
    curr_v = 0
    while len(curr_path):
        if edge_count[curr_v]:
            curr_path.append(curr_v)
            next_v = adj[curr_v].pop()
            edge_count[curr_v] -=1
            curr_v = next_v
        else:
            circuit.append(curr_v)
            curr_v = curr_path.pop();
    res = []
    for i in range(len(circuit)-1,-1, -1):
        res.append(circuit[i])
        if i:
            res.append(" -> ")
    return res

import random

class KnightTour:
    def __init__(self):
        self.cx = [1, 1, 2, 2, -1, -1, -2, -2]
        self.cy = [2, -2, 1, -1, 2, -2, 1, -1]

    def limits(self,x,y):
        return ((x >= 0 and y >= 0) and (x < 8 and y < 8));

    def is_empty(self, a, x, y):
        return self.limits(x, y) and a[y * 8 + x] < 0

    def degree(self, a, x, y):
        count = 0
        for i in range(len(self.cx)):
            if self.is_empty(a, x+self.cx[i], y + self.cy[i]):
                count += 1
        return count

    def nextMove(self, a, x, y):
        min_deg_idx = -1
        min_deg = (8 + 1)
        start = random.randint(0, 100) % 8
        for count in range(8):
            i = (start + count) % 8
            nx = x + self.cx[i]
            ny = y + self.cy[i]
            if self.is_empty(a, nx, ny):
                c = self.degree(a, nx, ny)
                if c < min_deg:
                    min_deg_idx = i
                    min_deg = c

        if min_deg_idx == -1:
            return None
        nx = x + self.cx[min_deg_idx]
        ny = y + self.cy[min_deg_idx]
        a[ny * 8 + nx] = a[y * 8 + x] + 1;
        return (nx, ny)

    def neighbour(self, x, y, xx, yy):
        for i in range(8):
            if x + self.cx[i] == xx and y + self.cy[i] == yy:
                return True
        return False

    def findClosedTour(self):
        a = [-1] * 64
        sx = random.randint(0, 100) % 8
        sy = random.randint(0, 100) % 8
        x = sx
        y = sy
        a[y * 8 + x] = 1
        for i in range(63):
            r = self.nextMove(a, x, y)
            if not r:
                return False
            x,y = r
        if not self.neighbour(x, y, sx, sy):
            return None
        return a

sol = KnightTour()
print(sol.findClosedTour())







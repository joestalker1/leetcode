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
class KnightTour:
    def __init__(self):
        self.cx = [1, 1, 2, 2, -1, -1, -2, -2]
        self.cy = [2, -2, 1, -1, 2, -2, 1, -1]

    def limits(self,x,y):
        return ((x >= 0 and y >= 0) and (x < 8 and y < 8));

    def is_empty(self, a, x, y):
        return self.limits(x, y) and a[y * 8 + x] < 0






adj = [0] * 3
adj[0] = [1]
adj[1] = [2]
adj[2] = [0]
print(hierholzer(adj))



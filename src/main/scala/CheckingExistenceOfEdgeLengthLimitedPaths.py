class Dsu:
    def __init__(self, n):
        self.p = [i for i in range(n)]
        self.rank = [1] * n

    def find(self, x):
        if self.p[x] != x:
            self.p[x] = self.find(self.p[x])
        return self.p[x]

    def union(self, x1, x2):
        p1 = self.find(x1)
        p2 = self.find(x2)
        if p1 == p2:
            return
        if self.rank[p1] > self.rank[p2]:
            self.p[p2] = p1
        elif self.rank[p2] > self.rank[p1]:
            self.p[p1] = p2
        else:
            self.p[p1] = p2
            self.rank[p2] += 1



class Solution:
    def distanceLimitedPathsExist(self, n: int, edgeList, queries):
        #sort queries by limit
        queries_by_dist = sorted([[x[0],x[1],x[2],i] for i,x in enumerate(queries)],key=lambda x:x[2])
        #sort by dist
        edge_by_dist = sorted(edgeList, key=lambda x:x[2])
        #union vertices if they are connected
        dsu = Dsu(n)
        res = [False] * len(queries)
        start = 0
        # go by limit in increasing order
        for s,e,limit,i in queries_by_dist:
            #union all edges if their distance is less than dist
            while start < len(edge_by_dist):
                p,q,dist = edge_by_dist[start]
                if dist >= limit:
                    break
                # connect two vetices
                dsu.union(p, q)
                start += 1
            # do s and e belong to one path?
            res[i] = dsu.find(s) == dsu.find(e)
        return res


sol = Solution()
print(sol.distanceLimitedPathsExist(13,
                                    [[9, 1, 53], [3, 2, 66], [12, 5, 99], [9, 7, 26], [1, 4, 78], [11, 1, 62],
                                     [3, 10, 50], [12, 1, 71], [12, 6, 63], [1, 10, 63], [9, 10, 88], [9, 11, 59],
                                     [1, 4, 37], [4, 2, 63], [0, 2, 26], [6, 12, 98], [9, 11, 99], [4, 5, 40],
                                     [2, 8, 25], [4, 2, 35], [8, 10, 9], [11, 9, 25], [10, 11, 11], [7, 6, 89],
                                     [2, 4, 99], [10, 4, 63]],
                                    [[9, 7, 65], [9, 6, 1], [4, 5, 34], [10, 8, 43], [3, 7, 76], [4, 2, 15], [7, 6, 52],
                                     [2, 0, 50], [7, 6, 62], [1, 0, 81], [4, 5, 35], [0, 11, 86], [12, 5, 50],
                                     [11, 2, 2], [9, 5, 6], [12, 0, 95], [10, 6, 9], [9, 4, 73], [6, 10, 48],
                                     [12, 0, 91], [9, 10, 58], [9, 8, 73], [2, 3, 44], [7, 11, 83], [5, 3, 14],
                                     [6, 2, 33]]))
#[true,false,false,true,true,false,false,true,false,true,false,true,false,false,false,true,false,true,false,true,true,true,false,true,false,false]
print(sol.distanceLimitedPathsExist(n=5, edgeList=[[0, 1, 10], [1, 2, 5], [2, 3, 9], [3, 4, 13]],
                                    queries=[[0, 4, 14], [1, 4, 13]]))  # [true,false]
print(sol.distanceLimitedPathsExist(n=3, edgeList=[[0, 1, 2], [1, 2, 4], [2, 0, 8], [1, 0, 16]],
                                    queries=[[0, 1, 2], [0, 2, 5]]))  # [false,true]

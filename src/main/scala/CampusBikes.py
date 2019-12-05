class Solution(object):
    def assignBikes(self, workers, bikes):
        if not workers or not bikes:
            return []
        buckets = [[] for _ in range(2001)]
        for i in range(len(workers)):
            for j in range(len(bikes)):
                d = abs(workers[i][0] - bikes[j][0]) + abs(workers[i][1] - bikes[j][1])
                buckets[d].append((i,j))

        res = [-1 for i in range(len(workers))]
        used_bikes = set()
        for bucket in buckets:
            for worker,bike in bucket:
                if res[worker] == -1 and bike not in used_bikes:
                    res[worker] = bike
                    used_bikes.add(bike)
        return res


sol = Solution()
print(sol.assignBikes(workers = [[0,0],[1,1],[2,0]], bikes = [[1,0],[2,2],[2,1]]))
print(sol.assignBikes(workers = [[0,0],[2,1]], bikes = [[1,2],[3,3]]))




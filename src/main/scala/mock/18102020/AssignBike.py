from collections import defaultdict


class Solution:
    def assignBikes(self, workers, bikes):
        def manh_dist(worker, bike):
            return abs(worker[0] - bike[0]) + abs(worker[1] - bike[1])

        q = defaultdict(list)
        for i in range(len(workers)):
            for j in range(len(bikes)):
                dist = manh_dist(workers[i], bikes[j])
                q[dist].append([i, j]) #worker, bike
        assigned_bikes = [-1] * len(workers)
        used_bikes = set()
        for dist in sorted(q.keys()):
            lst = q[dist]
            for w,b in lst:
                if assigned_bikes[w] == -1 and b not in used_bikes:
                    assigned_bikes[w] = b
                    used_bikes.add(b)
        return assigned_bikes


sol = Solution()
print(sol.assignBikes([[0, 0], [1, 1], [2, 0]], [[1, 0], [2, 2], [2, 1]]))

print(sol.assignBikes([[0,0],[2,1]], [[1,2],[3,3]]))

class Solution:
    def assignBikes(self, workers, bikes):
        def dist(x,y):
            return abs(x[0]-y[0]) + abs(x[1] - y[1])

        q = []
        for i in range(len(workers)):
            worker = workers[i]
            for j in range(len(bikes)):
                bike = bikes[j]
                q.append([dist(worker, bike), i, j])
        q.sort(key=lambda x:x[0])
        sum = 0
        seen = set()
        for d,w,b in q:
            if w in seen:
                continue
            seen.add(w)
            sum += d
            if len(seen) == len(workers):
                return sum
        return sum


sol = Solution()
print(sol.assignBikes([[0,0],[2,1]],[[1,2],[3,3]]))





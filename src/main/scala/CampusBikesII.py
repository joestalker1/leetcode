class Solution:
    def assignBikes(self, workers, bikes) -> int:

        def assign_bike(w, seen, mem):
            # use assign bike for every workers
            if w == len(workers):
                return 0
            k = (w, seen)
            if k in mem:
                return mem[k]
            p = 1
            min_sum = float('inf')
            # p helps to check if i bike is assigned
            for i in range(len(bikes)):
                #try every bike that is free assign to worker
                if (p & seen) == 0:
                    x,y = bikes[i]
                    x1,y1 = workers[w]
                    dist = abs(x - x1) + abs(y - y1)
                    min_sum = min(min_sum, dist + assign_bike(w + 1, seen | (1 << i), mem))
                p = p << 1
            mem[k] = min_sum
            return mem[k]
        return assign_bike(0, 0, {})


sol = Solution()
print(sol.assignBikes([[0,0],[1,0],[2,0],[3,0],[4,0]], [[0,999],[1,999],[2,999],[3,999],[4,999]]))
print(sol.assignBikes([[0, 0], [2, 1]], [[1, 2], [3, 3]]))  # 6
print(sol.assignBikes([[0, 0], [1, 1], [2, 0]], [[1, 0], [2, 2], [2, 1]]))  # 4

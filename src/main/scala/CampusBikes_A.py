class Solution:
    def assignBikes(self, workers, bikes):
        sorted_list = []
        for i, w in enumerate(workers):
            for j,b in enumerate(bikes):
                d = abs(w[0] - b[0]) + abs(w[1] - b[1])
                sorted_list.append([d,i,j])
        sorted_list.sort()
        ans = [-1] * len(workers)
        used_bikes = set()
        for d,w,b in sorted_list:
            if ans[w] != -1 or b in used_bikes:
                continue
            ans[w] = b
            used_bikes.add(b)
        return ans


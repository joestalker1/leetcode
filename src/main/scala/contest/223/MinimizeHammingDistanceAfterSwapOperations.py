from collections import defaultdict


class Dsu:
    def __init__(self, n):
        self.p = [i for i in range(n)]
        self.rank = [0] * n

    def find(self, x):
        if self.p[x] != x:
            self.p[x] = self.find(self.p[x])
        return self.p[x]

    def union(self, x1, x2):
        p1 = self.find(x1)
        p2 = self.find(x2)
        if p2 == p1:
            return
        if self.rank[p1] > self.rank[p2]:
            self.p[p2] = p1
        elif self.rank[p1] < self.rank[p2]:
            self.p[p1] = p2
        else:
            self.p[p1] = p2
            self.rank[p2] += 1


class Solution:
    def minimumHammingDistance(self, source, target, allowedSwaps):
        dsu = Dsu(len(source))
        for i, j in allowedSwaps:
            dsu.union(i, j)
        dist = 0
        par_to_members = defaultdict(list)
        for i in range(len(source)):
            p = dsu.find(i)
            par_to_members[p].append(i)
        freq = defaultdict(int)
        for _,lst in par_to_members.items():
            freq.clear()
            for i in lst:
                freq[source[i]] += 1
                freq[target[i]] -= 1
            dist += sum([v for _, v in freq.items() if v > 0])
        return dist


sol = Solution()
#print(sol.minimumHammingDistance([1, 2, 3, 4], [2, 1, 4, 5], [[0, 1], [2, 3]]))  # 1
# print(sol.minimumHammingDistance([50, 46, 54, 35, 18, 42, 26, 72, 75, 47, 50, 4, 54, 21, 18, 18, 61, 64, 100, 14],
#                                  [83, 34, 43, 73, 61, 94, 10, 68, 74, 31, 54, 46, 28, 60, 18, 18, 4, 44, 79, 92],
#                                  [[1, 8], [14, 17], [3, 1], [17, 10], [18, 2], [7, 12], [11, 3], [1, 15], [13, 17], [18,
#                                                                                                                      19],
#                                   [
#                                       0, 10], [15, 19], [0, 15], [6, 7], [7, 15], [19, 4], [7, 16], [14, 18], [8, 10], [
#                                       17, 0], [2, 13], [14, 10], [12, 17], [2, 9], [6, 15], [16, 18], [2, 16], [2, 6], [
#                                       4, 5], [17, 5], [10, 13], [7, 2], [9, 16], [15, 5], [0, 5], [8, 0], [11, 12], [9,
#                                                                                                                      7],
#                                   [
#                                       1, 0], [11, 17], [4, 6], [5, 7], [19, 12], [3, 18], [19, 1], [13, 18], [19, 6], [
#                                       13, 6], [6, 1], [4, 2]]))  # 14
print(sol.minimumHammingDistance([41, 37, 51, 100, 25, 33, 90, 49, 65, 87, 11, 18, 15, 18],
                                 [41, 92, 69, 75, 29, 13, 53, 21, 17, 81, 33, 19, 33, 32],
                                 [[0, 11], [5, 9], [6, 9], [5, 7], [8, 13], [4, 8], [12, 7], [8, 2], [13, 5], [0, 7], [
        6, 4], [8, 9], [4, 12], [6, 1], [10, 0], [10, 2], [7, 3], [11, 10], [5, 2], [11, 1], [3, 0], [8, 5], [12, 6], [
                                      2, 1], [11, 2], [4, 9], [2, 9], [10, 6], [12, 10], [4, 13], [13, 2], [11, 9], [3,
                                                                                                                     6], [
                                      0, 4], [1, 10], [5, 11], [12, 1], [10, 4], [6, 2], [10, 7], [3, 13], [4, 5], [13,
                                                                                                                    10], [
                                      4, 7], [0, 12], [9, 10], [9, 3], [0, 5], [1, 9], [5, 10], [8, 0], [12, 11], [11,
                                                                                                                   4], [
                                      7, 9], [7, 2], [13, 9], [12, 3], [8, 6], [7, 6], [8, 12], [4, 3], [7, 13], [0,
                                                                                                                  13], [
                                      2, 0], [3, 8], [8, 1], [13, 6], [1, 4], [0, 9], [2, 3], [8, 7], [4, 2], [9, 12]]))#12
print(sol.minimumHammingDistance([89, 43, 23, 35, 73, 21, 22, 97, 5, 11, 81, 67, 89, 93, 19, 74],
                                 [68, 43, 21, 46, 41, 21, 26, 5, 14, 71, 4, 30, 52, 2, 47, 74],
                                 [[12, 2], [3, 7], [9, 15], [5, 12], [6, 11], [13, 15], [4, 1], [12, 0], [9, 3],
                                  [11, 12], [4, 11], [7, 9], [7, 2], [9, 13], [15, 12], [3, 12], [12, 8], [13, 14],
                                  [11, 2], [8, 3], [14, 10], [0, 9], [12, 9]]))  # 11

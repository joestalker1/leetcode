import random

class Solution:
    def partition(self, points, i, j):
        dist = lambda i: points[i][0] ** 2 + points[i][1] ** 2

        # Partition by pivot A[i], returning an index mid
        # such that A[i] <= A[mid] <= A[j] for i < mid < j.
        oi = i
        pivot = dist(i)
        i += 1

        while True:
            while i < j and dist(i) < pivot:
                i += 1
            while i <= j and dist(j) >= pivot:
                j -= 1
            if i >= j: break
            points[i], points[j] = points[j], points[i]

        points[oi], points[j] = points[j], points[oi]
        return j

    def quick_select(self, points, i, j, K):
        if i >= j:
            return
        k = random.randint(i, j)
        points[k], points[i] = points[i], points[k]
        mid = self.partition(points, i, j)
        if K < mid - i + 1:
            self.quick_select(points, i, mid - 1, K)
        elif K > mid - i + 1:
            self.quick_select(points, mid + 1, j, K - (mid - i + 1))

    def kClosest(self, points, K: int):
        if not points or K == 0:
            return []

        self.quick_select(points, 0, len(points) - 1, K)
        return points[:K]


sol = Solution()
# print(sol.kClosest([[6, 10], [-3, 3], [-2, 5], [0, 2]], 3))
print(sol.kClosest([[3, 3], [5, -1], [-2, 4]], 2))

import random


class Solution:
    def kClosest(self, points, K):
        if not points or K == 0:
            return []

        dist = lambda i: points[i][0] ** 2 + points[i][1] ** 2

        def sort(i, j, k):
            if i > j:
                return
            mid = random.randint(i, j)
            points[i], points[mid] = points[mid], points[i]
            mid = partition(i, j)
            if mid - i + 1 < k:
                sort(mid + 1, j, k - (mid - i + 1))
            elif mid - i + 1 > k:
                sort(i, mid - 1, k)

        def partition(i, j):
            i1 = i
            pivot = dist(i1)
            i += 1
            while True:
                while i < j and dist(i) < pivot:
                    i += 1
                while i <= j and dist(j) > pivot:
                    j -= 1
                if i >= j:
                    break
                points[i], points[j] = points[j], points[i]
            points[i1], points[j] = points[j], points[i1]
            return j

        sort(0, len(points) - 1, K)
        return points[:K]


sol = Solution()
print(sol.kClosest(points=[[1, 3], [-2, 2]], K=1))

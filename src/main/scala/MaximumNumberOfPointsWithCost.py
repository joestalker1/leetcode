class Solution:
    def maxPoints(self, points) -> int:
        m = len(points)
        n = len(points[0])
        if m == 1:
            return max(points[0])
        if n == 1:
            return sum(points[i][0] for i in range(m))

        def left(arr):
            lft = [arr[0]] + [0] * (n - 1)
            for i in range(1, n):
                lft[i] = max(lft[i - 1] - 1, arr[i])
            return lft

        def right(arr):
            rgt = [0] * (n - 1) + [arr[-1]]
            for i in range(n - 2, -1, -1):
                rgt[i] = max(rgt[i + 1] - 1, arr[i])
            return rgt

        pre = points[0]
        for i in range(1, m):
            lft = left(pre)
            rgt = right(pre)
            cur = [0] * n
            for j in range(n):
                cur[j] = points[i][j] + max(lft[j], rgt[j])
            pre = cur[:]
        return max(cur[:])

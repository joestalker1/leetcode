class Solution:
    def longestIncreasingPath(self, matrix):
        if not matrix or not matrix[0]:
            return 0
        n = len(matrix)
        m = len(matrix[0])
        mem = {}
        def traverse(r,c, used, mem):
            if (r,c) in mem:
                return mem[(r,c)]
            max_len = 0
            a = matrix[r][c]
            for dr,dc in [[0,1],[0,-1],[1,0],[-1,0]]:
                r1 = r + dr
                c1 = c + dc
                if 0<= r1 < n and 0 <= c1 < m and matrix[r1][c1] > a and (r1,c1) not in used:
                    used.add((r1,c1))
                    path = 1 + traverse(r1,c1, used, mem)
                    max_len = max(max_len, path)
                    used.discard((r1,c1))
            mem[(r,c)] = max_len
            return mem[(r,c)]
        max_len = 0
        for r in range(n):
            for c in range(m):
                max_len = max(1 + traverse(r,c,set(), mem), max_len)
        return max_len



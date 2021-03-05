class Solution:
    def findPath(self, matrix):
        q = [[0, 0, 0]]
        n = len(matrix)
        m = len(matrix[0])
        seen = set((0, 0))
        while q:
            d, r, c = q.pop(0)
            if matrix[r][c] == 9:
                return d
            for dr, dc in [[0, 1], [1, 0], [-1, 0], [0, -1]]:
                nr = r + dr
                nc = c + dc
                if 0 <= nr < n and 0 <= nc < m and (nr, nc) not in seen and matrix[nr][nc] != 0:
                    seen.add((nr, nc))
                    q.append([d + 1, nr, nc])


sol = Solution()
print(sol.findPath([[1, 1, 0],
                    [1, 1, 0],
                    [1, 1, 9]]))

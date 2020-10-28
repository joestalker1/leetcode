class Solution:
    def longestIncreasingPath(self, matrix):
        if not matrix or not matrix[0]:
            return 0
        n = len(matrix)
        m = len(matrix[0])

        def backtrack(r, c, seen, mem):
            nonlocal n
            nonlocal m
            if (r,c) in mem:
                return mem[(r,c)]
            max_path = 0
            seen.add((r, c))
            for dr, dc in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
                nr = r + dr
                nc = c + dc
                if 0 <= nr < n and 0 <= nc < m:
                    if (nr, nc) in seen:
                        continue
                    if matrix[r][c] < matrix[nr][nc]:
                        cur_path = 1 + backtrack(nr, nc, seen, mem)
                        max_path = max(max_path, cur_path)
            seen.discard((r, c))
            mem[(r,c)] = max_path
            return max_path

        max_path = 0
        mem = {}
        for r in range(n):
            for c in range(m):
                cur_path = 1 + backtrack(r, c, set(), mem)
                max_path = max(cur_path, max_path)
        return max_path


sol = Solution()
print(sol.longestIncreasingPath([
  [3,4,5],
  [3,2,6],
  [2,2,1]
] ))
print(sol.longestIncreasingPath([
    [9, 9, 4],
    [6, 6, 8],
    [2, 1, 1]
]))

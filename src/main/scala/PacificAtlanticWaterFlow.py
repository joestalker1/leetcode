class Solution:
    def pacificAtlantic(self, matrix):
        if not matrix or not matrix[0]:
            return []
        num_rows = len(matrix)
        num_cols = len(matrix[0])
        atlantic_queue = []
        pacific_queue = []

        for i in range(num_rows):
            atlantic_queue.append((i, num_cols - 1))
            pacific_queue.append((i, 0))
        for i in range(num_cols):
            atlantic_queue.append((num_rows - 1, i))
            pacific_queue.append((0, i))

        def bfs(queue):
            reachable = set()
            while queue:
                r, c = queue.pop(0)
                reachable.add((r, c))
                for dx, dy in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
                    new_row = r + dx
                    new_col = c + dy
                    if (new_row,
                        new_col) in reachable or new_row < 0 or new_row >= num_rows or new_col < 0 or new_col >= num_cols:
                        continue
                    if matrix[new_row][new_col] < matrix[r][c]:
                        continue
                    queue.append((new_row, new_col))
            return reachable

        pacific_reachable = bfs(pacific_queue)
        atlantic_reachable = bfs(atlantic_queue)
        return pacific_reachable.intersection(atlantic_reachable)


sol = Solution()
print(sol.pacificAtlantic([[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]))
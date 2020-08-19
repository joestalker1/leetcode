from collections import defaultdict


class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        if x == 0 and y == 0:
            return 0

        seen = defaultdict(dict)
        seen[0][0] = 1

        q = [[0, 0, 0]]
        dx = [2, -2, 2, -2, 1, -1, 1, -1]
        dy = [1, 1, -1, -1, 2, 2, -2, -2]
        while q:
            m, x1, y1 = q.pop(0)
            if x1 == abs(x) and y1 == abs(y):
                return m

            for i in range(8):
                x2 = x1 + dx[i]
                y2 = y1 + dy[i]
                if abs(x2) + abs(y2) > 300 or x2 in seen and y2 in seen[x2] or x2 < -2 or y2 < -2:
                    continue
                q.append([m + 1, x2, y2])
                seen[x2][y2] = 1


sol = Solution()
#print(sol.minKnightMoves(2, 1))  # 1
print(sol.minKnightMoves(5, 5))  # 4

class Solution:
    def knightProbability(self, N: int, K: int, r: int, c: int):
        q = [[0, 1, r, c]]
        dx = [2, -2, 2, -2, 1, -1, 1, -1]
        dy = [1, 1, -1, -1, 2, 2, -2, -2]

        while q:
            p1, i, cur_r, cur_c = q.pop(0)
            if i == K:
                P = p1
                for p2,j, r1,c1 in q:
                    if j == K:
                        P += p2
                return P

            for i in range(9):
                next_r = cur_r + dx[i]
                next_c = cur_c + dy[i]
                if 0 <= next_r < N and 0 <= next_c < N:
                    q.append([p1 * 1 / 8, i + 1, next_r, next_c])
        return 0


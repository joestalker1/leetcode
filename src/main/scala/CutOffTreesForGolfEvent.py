from collections import deque

class Solution(object):
    def dist(self, forest, sr, sc, dr, dc):
        R, C = len(forest), len(forest[0])
        q = deque([(sr, sc, 0)])
        seen = {(sr, sc)}
        while q:
            r, c, d = q.popleft()
            if r == dr and c == dc:
                return d
            seen.add((r, c))
            for r1, c1 in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]:
                if 0 <= r1 < R and 0 <= c1 < C and (r1, c1) not in seen and forest[r1][c1]:
                    q.append((r1, c1, d + 1))
                    #seen.add((r1, c1))
        return -1

    def cutOffTree(self, forest):
        if not forest:
            return []
        heights = sorted((v, r, c) for r, row in enumerate(forest) for c, v in enumerate(row) if v > 1)
        sr, sc = 0, 0
        total = 0
        for v, r, c in heights:
            d = self.dist(forest, sr, sc, r, c)
            if d < 0:
                return -1
            total += d
            sr = r
            sc = c
        return total


sol = Solution()
print(sol.cutOffTree([[63750247, 40643210, 95516857, 89928134, 66334829, 58741187, 76532780, 45104329],
                      [3219401, 97566322, 9135413, 75944198, 93735601, 33923288, 50116695, 83660397],
                      [64460750, 53045740, 31903386, 78155821, 90848739, 38769489, 99349027, 85982891],
                      [30628785, 51077683, 70534803, 67460877, 91077770, 74197235, 5696362, 91459886],
                      [56105195, 82479378, 45937951, 52817583, 2768114, 43329099, 28189138, 21418604]]))

# print(sol.cutOffTree([
#     [1, 2, 3],
#     [0, 0, 0],
#     [7, 6, 5]
# ]))
print(sol.cutOffTree([
    [1, 2, 3],
    [0, 0, 4],
    [7, 6, 5]
]))

from collections import defaultdict

class Solution:
    def removeStones(self, stones):
        if not stones or not stones[0]:
            return 0
        cols = defaultdict(list)
        rows = defaultdict(list)
        for r,c in stones:
            cols[c].append([r,c])
            rows[r].append([r,c])

        def calc_max_moves(r, c, cols, rows, removed):
            if len(removed) == len(stones):
                return 0
            max_moves = 0
            for nr,nc in cols[c]:
                if (nr,nc) in removed:
                    continue
                removed.add((nr,nc))
                moves = 1 + calc_max_moves(nr,nc, cols, rows, removed)
                max_moves = max(max_moves, moves)
                removed.discard((nr,nc))
            for nr,nc in rows[r]:
                if (nr,nc) in removed:
                    continue
                removed.add((nr,nc))
                moves = 1 + calc_max_moves(nr,nc, cols, rows, removed)
                max_moves = max(max_moves, moves)
                removed.discard((nr,nc))
            return max_moves
        max_moves = 0
        for r,c in stones:
            removed = set()
            removed.add((r,c))
            moves = calc_max_moves(r,c,cols,rows, removed)
            max_moves = max(max_moves, moves)
        return max_moves


sol = Solution()
print(sol.removeStones([[0,0],[0,2],[1,1],[2,0],[2,2]]))
print(sol.removeStones([[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]]))



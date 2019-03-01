class Solution:
    def backtrack(self, board, word, pos, bpos, seen):
        def step(a1, a2, pos):
            tp = (a1, a2)
            seen.add(tp)
            res = self.backtrack(board, word, pos + 1, tp, seen)
            seen.remove(tp)
            return res

        i1, j1 = bpos
        if pos < len(word) and word[pos] != board[i1][j1]:
            return False

        if pos == len(word)-1:
            return True

        if (i1 - 1) >=0 and not((i1 - 1, j1) in seen):
            if step(i1 - 1, j1, pos):
                return True

        if (i1 + 1) < len(board) and not((i1 + 1, j1) in seen):
            if step(i1 + 1, j1, pos):
                return True

        if (j1 + 1) < len(board[0]) and not((i1, j1 + 1) in seen):
            if step(i1, j1 + 1, pos):
                return True

        if (j1 - 1) >= 0 and not((i1, j1 - 1) in seen):
            if step(i1, j1 - 1, pos):
                return True
        return False

    def exist(self, board, word: str) -> bool:
        if not board or not word:
            return False
        seen = set()
        for i in range(len(board)):
            for j in range(len(board[0])):
                if word[0] == board[i][j]:
                    tp = (i, j)
                    seen.add(tp)
                    if self.backtrack(board, word, 0, tp, seen):
                        return True
                    seen.remove(tp)
        return False


sol = Solution()
board1 = [
    ['A', 'B', 'C', 'E'],
    ['S', 'F', 'C', 'S'],
    ['A', 'D', 'E', 'E']
]
board2 = [["a"]]
print(sol.exist(board2, "b"))#false
print(sol.exist(board2, "a"))#true
print(sol.exist(board1, "ABCCE"))#true
print(sol.exist(board1, "SEE"))#true
print(sol.exist(board1, "ABCB"))#false

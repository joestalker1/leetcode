class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def valid(rows, diag, anti_diag,row,col):
            if col == 0:
                return True
            if row in rows or (row-col) in diag or (row + col) in anti_diag:
                  return False
            return True
        sol = []
        def backtrack(rows,diag,anti_diag,state, col):
            if col == n:
                board = []
                for i in range(n):
                    board.append(''.join(state[i]))
                sol.append(board)
                return
            for row in range(n):
                if row in rows or (row-col) in diag or (row + col) in anti_diag:
                    continue
                rows.add(row)
                diag.add(row-col)
                anti_diag.add(row+col)
                state[row][col] = 'Q'
                backtrack(rows, diag, anti_diag, state, col+1)
                rows.remove(row)
                diag.remove(row - col)
                anti_diag.remove(row + col)
                state[row][col] = '.'
        rows = set()
        diag = set()
        anti_diag = set()
        state = [['.']* n for _ in range(n)]
        backtrack(rows,diag,anti_diag, state,0)
        return sol
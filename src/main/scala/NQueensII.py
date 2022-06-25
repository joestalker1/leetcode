class Solution:
    def totalNQueens(self, n: int) -> int:
        solutions = [0]
        diag = set()
        cols = [-1] * n
        rows = set()
        anti_diag = set()

        def is_valid(rows, diag, anti_diag, r, c):
            return r not in rows and (r - c) not in diag and (r + c) not in anti_diag

        def to_str(cols):
            buf = []
            for i in range(n):
                buf.append(str(cols[i]))
            return '-'.join(buf)

        def find_uniq_path(sol, cols, rows, diag, anti_diag, c):
            if c == n:
                sol[0] += 1
                return
            for r in range(n):
                if is_valid(rows, diag, anti_diag, r, c):
                    rows.add(r)
                    cols[c] = r
                    anti_diag.add(r + c)
                    diag.add(r - c)
                    find_uniq_path(sol, cols, rows, diag, anti_diag, c + 1)
                    rows.discard(r)
                    cols[c] = -1
                    anti_diag.discard(r + c)
                    diag.discard(r - c)

        find_uniq_path(solutions, cols, rows, diag, anti_diag, 0)
        return solutions[0]
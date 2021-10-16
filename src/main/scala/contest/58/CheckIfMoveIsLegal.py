class Solution:
    def checkMove(self, board, rMove: int, cMove: int, color: str) -> bool:
        n = len(board)
        m = len(board[0])
        if color == 'W':
            bad_color = 'B'
        else:
            bad_color = 'W'
        min_good_line_len = 3
        board[rMove][cMove] = color
        #vertical
        cur_len = 0
        r = rMove - 1
        while r >= 0 and board[r][cMove] == bad_color:
            cur_len += 1
            r -= 1
        if r >= 0 and board[r][cMove] == color and cur_len + 2 >= min_good_line_len:
            return True

        cur_len = 0
        r = rMove + 1
        while r < 8 and board[r][cMove] == bad_color:
            cur_len += 1
            r += 1
        if r <= 7 and board[r][cMove] == color and cur_len + 2 >= min_good_line_len:
            return True

        cur_len = 0
        c = cMove - 1
        while c >= 0 and board[rMove][c] == bad_color:
            cur_len += 1
            c -= 1
        if c>=0 and board[rMove][c] == color and cur_len + 2 >= min_good_line_len:
            return True

        cur_len = 0
        c = cMove + 1
        while c < 8 and board[rMove][c] == bad_color:
            cur_len += 1
            c += 1
        if c <= 7 and board[rMove][c] == color and cur_len + 2 >= min_good_line_len:
            return True

        r = rMove - 1
        c = cMove - 1
        cur_len = 0
        while r >= 0 and c >= 0 and board[r][c] == bad_color:
            cur_len += 1
            r -= 1
            c -= 1
        if c >= 0 and r >= 0 and board[r][c] == color and cur_len + 2 >= min_good_line_len:
            return True

        cur_len = 0
        r = rMove - 1
        c = cMove + 1
        while r >= 0 and c < 8 and board[r][c] == bad_color:
            cur_len += 1
            r -= 1
            c += 1
        if r >= 0 and c < 8 and board[r][c] == color and cur_len + 2 >= min_good_line_len:
            return True

        cur_len = 0
        r = rMove + 1
        c = cMove + 1
        while r < 8 and c < 8 and board[r][c] == bad_color:
            cur_len += 1
            r += 1
            c += 1
        if r < 8 and c < 8 and board[r][c] == color and cur_len + 2 >= min_good_line_len:
            return True

        cur_len = 0
        r = rMove + 1
        c = cMove - 1
        while r < 8 and c >= 0 and board[r][c] == bad_color:
            cur_len += 1
            r += 1
            c -= 1
        if r < 8 and c >= 0 and board[r][c] == color and cur_len + 2 >= min_good_line_len:
            return True
        return False

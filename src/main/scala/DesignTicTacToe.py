from collections import defaultdict

class TicTacToe:

    def __init__(self, n: int):
        self.horiz = defaultdict(int)
        self.vert = defaultdict(int)
        self.diag = defaultdict(int)
        self.anti_diag = defaultdict(int)
        self.n = n

    def does_win(self, row, col, player):
        return self.horiz[(row, player)] == self.n or self.vert[(col, player)] == self.n or self.diag[
            player] == self.n or self.anti_diag[player] == self.n

    def move(self, row: int, col: int, player: int) -> int:
        self.horiz[(row, player)] += 1
        self.vert[(col, player)] += 1
        if row == col:
            self.diag[player] += 1
        if row == self.n - col - 1:
            self.anti_diag[player] += 1
        if self.does_win(row, col, player):
            return player
        return 0

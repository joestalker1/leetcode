class NQueens:
    def __init__(self):
        self.x = [0] * 9 # x[i] row in i-th column
        self.lineCounter = 0

    def place(self, queen, row):
        for q in range(1, queen): #number queens
            #if a queen has the same row or the same diagonal?
            if self.x[q] == row or abs(self.x[q] - row) == abs(q - queen):
                return False
        return True

    def search(self, queen, a, b):
        for row in range(1, 9):
            if self.place(queen, row):
                self.x[queen] = row
                if queen == 8 and self.x[b] == a:
                    self.lineCounter += 1
                    print(self.x)
                else:
                    self.search(queen + 1, a, b)
        return []


sol = NQueens()
b = 2
a = 2
print(sol.search(1, a, b))



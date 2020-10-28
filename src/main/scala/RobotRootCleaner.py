class Robot:
    def __init__(self, grid, pos):
        self.grid = grid
        self.start = pos
        # 0 is up, 1 is right,2 is down,3 is left
        self.dir = 0

    def move(self):
        r, c = self.start
        if self.dir == 0:
            if r - 1 < 0 or self.grid[r - 1][c] == 0:
                return False
            self.start = [r - 1, c]
        elif self.dir == 1:
            n = len(self.grid[0])
            if c + 1 == n or self.grid[r][c + 1] == 0:
                return False
            self.start = [r, c + 1]
        elif self.dir == 2:
            n = len(self.grid)
            if r + 1 == n or self.grid[r + 1][c] == 0:
                return False
            self.start = [r + 1, c]
        else:
            if c - 1 < 0 or self.grid[r][c - 1] == 0:
                return False
            self.start = [r, c - 1]
        self.print_grid()
        print('')
        return True

    def turnLeft(self):
        if self.dir == 0:
            self.dir = 3
        elif self.dir == 1:
            self.dir = 0
        elif self.dir == 2:
            self.dir = 1
        else:
            self.dir = 2

    def turnRight(self):
        if self.dir == 0:
            self.dir = 1
        elif self.dir == 1:
            self.dir = 2
        elif self.dir == 2:
            self.dir = 3
        else:
            self.dir = 0

    def clean(self):
        r, c = self.start
        if self.grid[r][c] == 1:
            self.grid[r][c] = 2

    def print_grid(self):
        n = len(self.grid)
        m = len(self.grid[0])
        for i in range(n):
            s = []
            for j in range(m):
                if self.grid[i][j] == 2:
                    s.append('.')
                elif self.grid[i][j] == 0:
                    s.append('X')
                else:
                    s.append(' ')
            print(''.join(s))



class Solution(object):
    def cleanRoom(self, robot):
        def go_back():
            robot.turnRight()
            robot.turnRight()
            robot.move()
            robot.turnRight()
            robot.turnRight()

        def backtrack(cell=(0, 0), d=0):
            visited.add(cell)
            robot.clean()
            # going clockwise : 0: 'up', 1: 'right', 2: 'down', 3: 'left'
            for i in range(4):
                new_d = (d + i) % 4
                new_cell = (cell[0] + directions[new_d][0], cell[1] + directions[new_d][1])

                if not new_cell in visited and robot.move():
                    backtrack(new_cell, new_d)
                    go_back()
                # turn the robot following chosen direction : clockwise
                robot.turnRight()

        # going clockwise : 0: 'up', 1: 'right', 2: 'down', 3: 'left'
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        visited = set()
        backtrack()


robot = Robot([[1, 1, 1, 1, 1, 0, 1, 1], [1, 1, 1, 1, 1, 0, 1, 1], [1, 0, 1, 1, 1, 1, 1, 1], [0, 0, 0, 1, 0, 0, 0, 0],
               [1, 1, 1, 1, 1, 1, 1, 1]], [1, 3])

sol = Solution()
print(sol.cleanRoom(robot))
print(robot.grid)

class Solution(object):
    def is_valid(self, ghosts, x, y):
        for ghost in ghosts:
            gx, gy = ghost[1], ghost[0]
            if gy == y and gx == x:
                return False
            if gy - 1 >= 0 and gy - 1 == y and gx == x:
                return False
            if gy + 1 == y and gx == x:
                return False
            if gx - 1 >= 0 and gx - 1 == x and gy == y:
                return False
            if gx + 1 == x and gy == y:
                return False

        return True

    def may_move(self, ghosts, x, y, targets):
        ty = targets[0]
        tx = targets[1]
        wayx = []
        if x > tx:
            for a in range(x - 1, tx + 1, -1):
                wayx.append([a, y])
        elif x < tx:
            for a in range(x + 1, tx + 1):
                wayx.append([a, y])
        wayy = []
        if y > ty:
            for a in range(y - 1, ty + 1, -1):
                wayy.append([x, a])
        elif y < ty:
            for a in range(y + 1, ty + 1):
                wayy.append([x, a])

        for way in wayx:
            y0, x0 = way[1], way[0]
            if not self.is_valid(ghosts, x0, y0):
                return False
        for way in wayy:
            y0, x0 = way[1], way[0]
            if not self.is_valid(ghosts, x0, y0):
                return False
        return True

    def escapeGhosts(self, ghosts, targets):
        return self.may_move(ghosts, 0, 0, targets)


sol = Solution()
print(sol.escapeGhosts([[-1,2],[0,1],[-2,3],[0,1],[-5,0]], [-2,0]))

print(sol.escapeGhosts([[1, 0], [0, 3]], [0, 1]))

print(sol.escapeGhosts([[1, 0]], [2, 0]))

print(sol.escapeGhosts([[2,0]], [1, 0]))
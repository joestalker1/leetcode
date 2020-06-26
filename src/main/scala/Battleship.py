class Ship:
    def __init__(self, top_left, bottom_right):
        self.top_left = [top_left[0], top_left[1]]
        self.bottom_right = [bottom_right[0], bottom_right[1]]
        r1, c1 = self.top_left
        r2, c2 = self.bottom_right
        w = ord(r2) - ord(r1) + 1
        h = ord(c2) - ord(c1) + 1
        self.cells = w * h
        self.hits = 0

    def hit(self, rc):
        r, c = rc
        r1, c1 = self.top_left
        r2, c2 = self.bottom_right
        if r1 <= r <= r2 and c1 <= c <= c2:
            self.hits += 1
            return True
        return False

    def is_sunk(self):
        return self.cells == self.hits


class Solution:
    def solution(self, N, S, T):
        coords = S.split(',')
        ships = []
        for coord in coords:
            rc = coord.split(' ')
            ship = Ship(rc[0],rc[1])
            ships.append(ship)

        hits = T.split(' ')
        hit_count = 0
        for hit in hits:
            for ship in ships:
                ship.hit([hit[0],hit[1]])

        return [sum([1 for ship in ships if ship.is_sunk()]), sum([s.hits for s in ships if not s.is_sunk()]) ]


sol = Solution()
print(sol.solution(3, '1A 1B,2C 2C', '1B'))
print(sol.solution(4,'1B 2C,2D 4D', '2B 2D 3D 4D 4A'))




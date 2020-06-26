class Solution:
    def gcd(self, a, b):
        if b == 0:
            return a
        return self.gcd(b, a % b)

    def solution(self, ax, ay, bx, by):
        dx = bx - ax
        dy = by - ay

        rx = dy
        ry = -dx
        gcd = abs(self.gcd(rx, ry))

        rx //= gcd
        ry //= gcd

        return [bx + rx, by + ry]


sol = Solution()
print(sol.solution(-1, 3, 3, 1))

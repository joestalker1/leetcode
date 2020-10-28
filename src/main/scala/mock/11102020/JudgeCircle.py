class Solution:
    def judgeCircle(self, moves):
        if not moves:
            return True
        r = 0
        c = 0
        for move in moves:
            if move == 'L':
                c -= 1
            elif move=='R':
                c += 1
            elif move == 'D':
                r += 1
            else:
                r -= 1
        return r == 0 and c == 0

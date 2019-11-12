class Solution(object):
    def queensAttacktheKing(self, queens, king):
        if not queens or not king:
            return []
        threat = set()
        for queen in queens:
            y,x = queen
            threat.add((y,x))
        ky,kx = king
        res = []
        y = ky - 1
        #top
        while y >= 0:
            if (y,kx) in threat:
                res.append([y,kx])
                break
            y -= 1
        #bottom
        y = ky + 1
        while y < 64:
            if (y, kx) in threat:
                res.append([y,kx])
                break
            y += 1
        #right
        x = kx + 1
        while x < 64:
            if (ky, x) in threat:
                res.append([ky, x])
                break
            x += 1
        #left
        x = kx - 1
        while x >= 0:
            if (ky, x) in threat:
                res.append([ky, x])
                break
            x -= 1
        #top left:
        x = kx - 1
        y = ky - 1
        while x >= 0 and y >= 0:
            if (y,x) in threat:
                res.append([y,x])
                break
            x -= 1
            y -= 1
        #top right
        y = ky - 1
        x = kx + 1
        while y >= 0 and x < 64:
            if (y, x) in threat:
                res.append([y,x])
                break
            y -= 1
            x += 1
        #bottom left
        y = ky + 1
        x = kx - 1
        while y < 64 and x >= 0:
            if (y,x) in threat:
                res.append([y,x])
                break
            y += 1
            x -= 1
        #bottom right
        y = ky + 1
        x = kx + 1
        while x < 64 and y < 64:
            if (y,x) in threat:
                res.append([y,x])
                break
            y += 1
            x += 1
        return res

sol = Solution()
print(sol.queensAttacktheKing(queens = [[0,0],[1,1],[2,2],[3,4],[3,5],[4,4],[4,5]], king = [3,3]))
print(sol.queensAttacktheKing(queens = [[0,1],[1,0],[4,0],[0,4],[3,3],[2,4]], king = [0,0]))




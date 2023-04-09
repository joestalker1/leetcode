from collections

class Solution:
    def isRectangleCover(self, rectangles) -> bool:
        if not rectangles:
            return True

        xy_coord = collections.defaultdict(int)

        for x1,y1,x2,y2 in rectangles:
            xy_coord[(x1,y1)] += 1
            xy_coord[(x2,y2)] += 1
            xy_coord[(x1,y2)] -= 1
            xy_coord[(x2,y1)] -= 1

        cur_sum = 0
        for x,y in sorted(xy_coord.keys()):
            cur_sum += xy_coord[(x,y)]
            if abs(xy_coord[(x,y)]) == 1:
                cnt += 1
            elif abs(xy_coord[(x,y)]) != 1 and xy_coord[(x,y)] != 0:
                return False
        return cnt == 4
class Solution:
    def isRectangleOverlap(self, rec1, rec2):
        if not rec1 or not rec2:
            return False
        x1,y1,x2,y2 = rec1
        x3,y3,x4,y4 = rec2
        # one rect is upper then other
        if y2 <= y3 or y4 <= y1:
            return False
        if x2 <= x3 or x4 <= x1:
            return False
        return True


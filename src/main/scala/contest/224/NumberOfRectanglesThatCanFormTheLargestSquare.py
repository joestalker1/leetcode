class Solution:
    def countGoodRectangles(self, rectangles):
        maxLen = 0
        for l,w in rectangles:
            min_w = min(l,w)
            maxLen = max(maxLen, min_w)
        rects = 0
        for l,w in rectangles:
            if min(l,w)==maxLen:
                rects += 1
        return rects


sol = Solution()
print(sol.countGoodRectangles([[5,8],[3,9],[5,12],[16,5]]))


class Solution:
    def findMinArrowShots(self, points) -> int:
        points.sort(key=lambda p: p[1])
        arrows = 1
        i = 0
        end = points[0][1]
        for i in range(len(points)):
            if points[i][0] > end or points[i][1] < end:
                arrows += 1
                end = points[i][1]
        return arrows


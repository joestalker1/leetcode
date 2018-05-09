from math import sqrt
class Solution:
    def dist(self, p1, p2):
        x1,y1 = (p1[0],p1[1])
        x2,y2 = (p2[0],p2[1])
        d = (x2 - x1)*(x2 - x1) + (y2 - y1)*(y2 - y1)
        return sqrt(d)

    def numberOfBoomerangs(self, points):
        count = 0
        for i in range(len(points)):
            for j in range(len(points)):
                if i != j:
                    for k in range(len(points)):
                        if k != i and k != j:

                            d1 = self.dist(points[i], points[j])
                            d2 = self.dist(points[i], points[k])
                            if d1 == d2:
                               count += 1
        return count


sol = Solution()
print(sol.numberOfBoomerangs([[0,0],[1,0],[2,0]]))




from collections import defaultdict

class Solution:
    def maxPoints(self, points) -> int:
        if len(points) < 2:
            return len(points)

        def gcd(a, b):
            if b == 0:
                return a
            return gcd(b, a % b)

        def norm_slope(a, b):
            run = b[0] - a[0]
            if run == 0:
                return (1, 0)
            rise = b[1] - a[1]
            gcd_ = gcd(rise, run)
            return (rise // gcd_, run // gcd_)

        max_points = 0
        for i in range(len(points) - 1):
            slopes = defaultdict(lambda: 1)
            for j in range(i + 1, len(points)):
                slope = norm_slope(points[i], points[j])
                slopes[slope] += 1
            max_points = max(max_points, max(slopes.values()))

        return max_points
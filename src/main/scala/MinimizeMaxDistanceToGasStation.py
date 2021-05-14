class Solution:
    def minmaxGasDist(self, stations, k: int) -> float:
        dist = []
        for i in range(1, len(stations)):
            dist.append(stations[i] - stations[i - 1])
        lo = 0
        hi = sum(dist)

        def count_stations(dist, d):
            return sum([int(dst / d) for dst in dist])

        while hi - lo > 10 ** (-6):
            m = lo + (hi - lo) / 2.0
            if count_stations(dist, m) <= k:
                hi = m
            else:
                lo = m
        return hi

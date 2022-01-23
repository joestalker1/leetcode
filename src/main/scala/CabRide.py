class Solution:
    def ride(self, cabs, n):

        def count_ride(min_cost):
            rides = 0
            for i in range(len(cabs)):
                if min_cost < cabs[i] or rides >= n:
                    break
                possible_rides = min_cost // cabs[i]
                rides += possible_rides
            return rides

        cabs.sort()

        lo = 0
        hi = cabs[0] * n
        while lo < hi:
            cost = lo + (hi - lo)//2
            rides = count_ride(cost)
            if rides < n:
                lo = cost + 1
            else:
                hi = cost
        return lo


sol = Solution()
assert sol.ride([1,2], 3) == 2
assert sol.ride([1,3,5,7,8], 10) == 7
assert sol.ride([3,4,8], 3) == 6

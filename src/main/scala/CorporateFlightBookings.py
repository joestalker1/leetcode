class Solution:
    def corpFlightBookings(self, bookings, n):
        res = [0] * n
        for a, b, w in bookings:
            res[a - 1] += w
            if b < n:
                res[b] -= w
        for i in range(1, n):
            res[i] += res[i-1]
        return res


sol = Solution()
print(sol.corpFlightBookings([[1,2,10],[2,3,20],[2,5,25]], n = 5))


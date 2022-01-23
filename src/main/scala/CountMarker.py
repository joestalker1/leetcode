class Solution:
    def marker(self, coord):
        coord.sort(key=lambda x: x[0])
        last_interval = None
        marker = 0
        for interval in coord:
            if not last_interval:
                last_interval = interval
            elif last_interval[1] >= interval[0]:
                last_interval[1] = interval[1]
            else:
                marker += last_interval[1] - last_interval[0] + 1
                last_interval = interval
        return marker + last_interval[1] - last_interval[0] + 1


sol = Solution()
print(sol.marker([[4,7],[-1,5],[3,6]]))





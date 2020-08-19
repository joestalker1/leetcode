class Solution:
    def merge(self, intervals):
        if not intervals:
            return intervals

        def is_overlapped(int1, int2):
            s1, e1 = int1
            s2, e2 = int2
            return s1 <= s2 <= e1 or s2 <= s1 <= e2

        def merge_with(int1, int2):
            s1, e1 = int1
            s2, e2 = int2
            return [min(s1, s2), max(e1, e2)]

        ranges = intervals
        while True:
            if len(ranges) > 1:
                new_ranges = []
                i = 0
                while i < len(ranges):
                    if i + 1 < len(ranges) and is_overlapped(ranges[i], ranges[i+1]):
                        merged = merge_with(ranges[i], ranges[i+1])
                        new_ranges.append(merged)
                        i += 2
                    else:
                        new_ranges.append(ranges[i])
                        i += 1
                if len(new_ranges) == len(ranges):
                    ranges = new_ranges
                    break
                ranges = new_ranges
            else:
                break
        return ranges



sol = Solution()
print(sol.merge( [[1,3],[5,7],[4,6]]))





class Solution:
    def countWays(self, ranges) -> int:
        if len(ranges) == 1:
            return 2
        # find not overlaped ranges
        sorted_ranges = sorted(ranges, key=lambda x: x[0])
        merged = []
        MOD = 10 ** 9 + 7
        for a, b in sorted_ranges:
            if not merged:
                merged.append([a, b])
            elif merged[-1][1] > a:
                merged[-1][1] = max(merged[-1][1], b)
            else:
                merged.append([a, b])
        grp_num = len(merged)
        return (2 ** grp_num) % MOD



sol = Solution()
print(sol.countWays([[6,10],[5,15]]))#2
print(sol.countWays([[0,0],[8,9],[12,13],[1,3]]))#16
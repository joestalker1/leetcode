class Solution:
    def minCost(self, colors: str, neededTime) -> int:
        if not colors or not neededTime:
            return []
        left,right = 0,0
        total_time = 0
        max_color_time = 0
        for i in range(len(neededTime)):
            if i > 0 and colors[i] != colors[i-1]:
                max_color_time = 0
            total_time += min(neededTime[i], max_color_time)
            max_color_time = max(max_color_time, neededTime[i])
        return total_time
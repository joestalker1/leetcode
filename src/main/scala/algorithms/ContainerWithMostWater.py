class Solution:
    def maxArea(self, height) -> int:
        if len(height) < 0:
            return 0
        if len(height) == 2:
            return min(height) * 1
        max_cap = 0
        l = 0
        r = len(height) - 1
        while l < r:
            max_cap = max(max_cap, (r - l) * min(height[r], height[l]) )
            if height[l] < height[r]:
                l += 1
            elif height[l] > height[r]:
                r -= 1
            else:
                l += 1
                r -= 1
        return max_cap

class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts, verticalCuts) -> int:
        MOD = 10 ** 9 + 7
        if not horizontalCuts and not verticalCuts:
            return (h * w) % MOD
        horizontalCuts.sort()
        verticalCuts.sort()
        horizontalCuts = [0] + horizontalCuts + [h]
        verticalCuts = [0] + verticalCuts + [w]
        max_width = 0
        max_height = 0
        for i in range(len(horizontalCuts)-1):
            max_width = max(max_width, horizontalCuts[i+1] - horizontalCuts[i])
        for i in range(len(verticalCuts)-1):
            max_height = max(max_height, verticalCuts[i+1] - verticalCuts[i])
        return (max_width % MOD * max_height % MOD) % MOD
class Solution:
    def minimumPerimeter(self, neededApples: int) -> int:
        d = 1
        while neededApples > 0:
            apples = 12 * d
            apples += 8 * ((2*d - 1)* d - ((d+1) * d) // 2)
            neededApples -= apples
            d += 1
        return (d-1) * 8

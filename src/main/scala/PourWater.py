class Solution:
    def find_min(self, heights, v, d):
        i = v
        res = -1
        #look up leftmost/rightmost min
        while 0 <= (i + d) < len(heights) and heights[i + d] <= heights[i]:
            if heights[i + d] < heights[i]:
                res = i + d
            i += d
        if res != -1:
            return res
        return -1

    def pourWater(self, heights, V: int, K: int):
        if not heights or V == 0:
            return heights
        for v in range(V):
            left = self.find_min(heights, K, -1)
            if left >= 0:
                heights[left] += 1
            else:
                right = self.find_min(heights, K, 1)
                if right >= 0:
                    heights[right] += 1
                else:
                    heights[K] += 1

        return heights


sol = Solution()
# print(sol.pourWater([14,9,10,9,7,9,7,5,3,2],7,9))

print(sol.pourWater([1, 2, 3, 4, 3, 2, 1, 2, 3, 4, 3, 2, 1], 10, 2))
# [4,4,4,4,3,3,3,3,3,4,3,2,1]

# print(sol.pourWater([1,2,3,4,3,2,1,2,3,4,3,2,1],2, 5))
# [1,2,3,4,3,3,2,2,3,4,3,2,1]
# print(sol.pourWater([14,10,10,3,13,1,2,1,2,5],1,0))
# print(sol.pourWater([3, 1, 3], 5, 1))  # [4,4,4]
# print(sol.pourWater([3, 1, 3], 2, 2))
print(sol.pourWater([1, 2, 3, 4], 2, 2))
# [2,3,3,4]
# print(sol.pourWater([2, 1, 1, 2, 1, 2, 2], 4, 3))

class Solution:
    def largestSubmatrix(self, matrix):
        n = len(matrix)
        m = len(matrix[0])
        height = [0] * m
        max_area = 0
        for i in range(n):
            # calculate pillar heights
            for j in range(m):
                if matrix[i][j] == 0:
                    height[j] = 0
                else:
                    height[j] += 1
            #sort in increasing order but keeping orignal array
            sorted_height = sorted(height)
            # go from left to right: rightmost items are higher then leftmost
            for j in range(m):
                # height * number of rightmost items.
                max_area = max(max_area, sorted_height[j] * (m - j))
        return max_area


sol = Solution()
print(sol.largestSubmatrix([[0, 0, 1], [1, 1, 1], [1, 0, 1]]))#4
print(sol.largestSubmatrix(
    [[1, 1, 0, 0, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1],
     [1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 1, 1, 1, 1],
     [1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 0]]
))#40

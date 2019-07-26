class Solution:
    def sortedSquares(self, A):
        if not A:
            return []
        squares = []
        for a in A:
            squares.append(a * a)
        squares.sort()
        return squares


sol = Solution()
print(sol.sortedSquares([-4,-1,0,3,10]))
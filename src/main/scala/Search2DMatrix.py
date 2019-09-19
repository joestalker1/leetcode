class Solution:
    def search(self, row, target, s, e):
        if s > e:
            return False
        mid = s + (e - s) // 2
        if row[mid] > target:
            return self.search(row, target, s, mid - 1)
        elif row[mid] < target:
            return self.search(row, target, mid + 1, e)
        return True

    def searchMatrix(self, matrix, target):
        if not matrix or len(matrix) == 0:
            return False
        for row in matrix:
            if len(row) and row[0] <= target <= row[-1]:
                return self.search(row, target, 0, len(row) - 1)
        return False


sol = Solution()
print(sol.searchMatrix([[1]], 1))
print(sol.searchMatrix([[]], 1))

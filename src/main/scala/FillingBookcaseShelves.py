class Solution:
    def minHeightShelves(self, books, shelf_width):
        dp = [0] # for previous book
        for i in range(len(books)):
            # book on new shelf
            cur_width = books[i][0]
            # height if place books[i] on new shelf
            height = dp[i] + books[i][1]
            max_height = books[i][1]
            j = i - 1
            while j >= 0 and cur_width + books[j][0] <= shelf_width:
                cur_width += books[j][0]
                max_height = max(max_height, books[j][1])
                # height if place books[i] on the current shelf
                # dp[j] contains
                height = min(height, dp[j] + max_height)
                j -= 1
            dp.append(min(height, dp[i] + books[i][1]))
        return dp[-1]

sol = Solution()
print(sol.minHeightShelves([[1,1],[2,3],[2,3],[1,1],[1,1],[1,1],[1,2]], 4))

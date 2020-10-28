class Solution:
    def minHeightShelves(self, books, shelf_width):
        if not books:
            return 0
        # first book at shelf
        dp = [books[0][1]]
        for i in range(1, len(books)):
            cur_width = books[i][0]
            # height if place books[i] on new shelf
            height = dp[i - 1] + books[i][1]
            max_height = books[i][1]
            j = i - 1
            # try to place 0 ... i -1 books on the same self where i book takes place
            while j >= 0 and cur_width + books[j][0] <= shelf_width:
                cur_width += books[j][0]
                max_height = max(max_height, books[j][1])
                # height if place books[i] on the current shelf
                # dp[j] points out shelf height of dp[i-2] and dp[j] + max_height is height if we place i and i -1 books at the same shelf
                if j - 1 >= 0:
                    height = min(height, dp[j - 1] + max_height)
                else:
                    height = min(height, max_height)
                j -= 1
            dp.append(min(height, dp[i - 1] + books[i][1]))
        return dp[-1]


sol = Solution()
print(sol.minHeightShelves([[1,1],[2,3],[2,3],[1,1],[1,1],[1,1],[1,2]], 4))

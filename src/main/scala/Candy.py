class Solution:
    def candy(self, ratings) -> int:
        if not ratings:
            return 0
        candies = [1] * len(ratings)
        for i in range(len(ratings)):
            if i > 0 and ratings[i] > ratings[i-1]:
                candies[i] = candies[i-1] + 1
        right = [1] * len(ratings)
        for i in range(len(ratings) - 1,-1,-1):
            if i + 1 < len(ratings) and ratings[i] > ratings[i+1]:
                candies[i] = max(candies[i], candies[i+1] + 1)
        return sum([candies[i] for i in range(len(ratings))])
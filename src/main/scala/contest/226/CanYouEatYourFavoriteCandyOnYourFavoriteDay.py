class Solution:
    def canEat(self, candiesCount, queries):
        prefix = [0] * len(candiesCount)
        prefix[0] = candiesCount[0]
        for i in range(1, len(candiesCount)):
            prefix[i] = prefix[i - 1] + candiesCount[i]
        prefix = [0] + prefix
        ans = [False] * len(queries)
        #go through queries
        for i in range(len(queries)):
            candy,day,cap = queries[i]
            maxDays = prefix[candy + 1] - 1 #eat one candy per day, d starts from 0
            minDays = prefix[candy] // cap # for days I eat candies of type candy - 1
            ans[i] = minDays <= day <= maxDays
        return ans


class Solution:
    def minSkips(self, dist: List[int], speed: int, hoursBefore: int) -> int:
        # assert self._minSkips([1,1,1],1,3) == 0, 'enough time'
        # assert self._minSkips([1,1,1],1,2) == -1, 'not enough time'
        # assert self._minSkips([3,2,1],2,3) == 0, 'enough time'
        return self._minSkips(dist, speed, hoursBefore)

    def _minSkips(self, dist: List[int], speed: int, hoursBefore: int) -> int:
        if sum(dist) / speed > hoursBefore:
            return -1
        # dp[i][k] = minimum skip to cross i roads
        n = len(dist)
        # dp contains dist for 0 to i roads and apply j skips
        # n+1 roads
        dp = [[0] * (n + 1) for _ in range(n + 1)]
        for k in range(n + 1):
            for i in range(n):
                # calculate distance for i+1 roaad if we don't skip rest,ceil(a/b) => (a+b-1)/b
                dp[i + 1][k] = (dp[i][k] + dist[i] + speed - 1) // speed * speed
                if k > 0:
                    # count distance if we skip rest
                    dp[i + 1][k] = min(dp[i + 1][k], dp[i][k - 1] + dist[i])
            if dp[n][k] <= speed * hoursBefore:
                return k
        return -1
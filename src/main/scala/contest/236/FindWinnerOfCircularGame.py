class Solution:
    def findTheWinner(self, n: int, k: int):
        if n <= k:
            return None
        q = [i for i in range(1, n + 1)]
        cur = 0
        s = k - 1
        while len(q) > 1:
            cur = (cur + s) % len(q)
            q.pop(cur)
        return q[0]

sol = Solution()
print(sol.findTheWinner(6,5))#1
print(sol.findTheWinner(5,2))#3




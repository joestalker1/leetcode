class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        if n == 1:
            if k == 1:
                return 0
            return 1
        else:
            half = 2 ** (n - 2)
            if k <= half:
                return self.kthGrammar(n - 1, k)
            res = self.kthGrammar(n-1, k - half)
            if res == 0:
                return 1
            return 0


sol = Solution()
print(sol.kthGrammar(3, 4))#0
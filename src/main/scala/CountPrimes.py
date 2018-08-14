class Solution:
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        composites = set([0, 1])
        i = 2
        while (i * i) < n:
            if i not in composites:
                b = 2 * i
                while b < n:
                    if b not in composites:
                        composites.add(b)
                    b = b + i
            i += 1
        r = n - len(composites)
        if r < 0:
            r = 0
        return r


n = input()
sol = Solution()
print(sol.countPrimes(int(n)))

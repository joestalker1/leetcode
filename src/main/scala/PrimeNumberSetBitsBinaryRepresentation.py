class Solution:
    def count_bin_one(self,a):
        ones = 0
        while a > 0:
            if a & 1:
                ones += 1
            a = a >> 1
        return ones

    def countPrimeSetBits(self, L, R):
        if L >= R:
            return 0
        res = 0
        primes = [2, 3, 5, 7, 11, 13, 17, 19]
        for a in range(L, R + 1):
            num_of_one = self.count_bin_one(a)
            if num_of_one in primes:
                res += 1
        return res


sol = Solution()
print(sol.countPrimeSetBits(6, 10))
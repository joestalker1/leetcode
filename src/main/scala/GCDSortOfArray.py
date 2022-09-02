class UnionFind:
    def __init__(self, n):
        self.par = [i for i in range(n)]
        self.rank = [0] * n

    def find(self, x):
        if self.par[x] != x:
            self.par[x] = self.find(self.par[x])
        return self.par[x]

    def union(self, x1, x2):
        p1 = self.find(x1)
        p2 = self.find(x2)
        if p1 == p2:
            return
        if self.rank[p1] > self.rank[p2]:
            self.par[p2] = p1
        elif self.rank[p2] > self.rank[p1]:
            self.par[p1] = p2
        else:
            self.par[p1] = p2
            self.rank[p2] += 1


class Solution:
    def sieve(self, n):
        spf = [i for i in range(n)]
        for i in range(2, n):
            if spf[i] != i:
                continue
            for j in range(i * i, n, i):
                if spf[j] > i:
                    spf[j] = i
        return spf

    def get_prime_factors(self, spf, num):
        while num > 1:
            yield spf[num]
            num = num // spf[num]

    def gcdSort(self, nums) -> bool:
        if not nums:
            return False
        if len(nums) == 1:
            return True

        max_val = max(nums)
        spf = self.sieve(max_val + 1)
        uf = UnionFind(max_val + 1)
        for num in nums:
            for p in self.get_prime_factors(spf, num):
                #connect every num factor with num itself
                uf.union(p, num)

        sorted_nums = sorted(nums)
        for x, y in zip(nums, sorted_nums):
            #check if we can exchange this 2 numbers if they belong to one group.
            if uf.find(x) != uf.find(y):
                return False
        return True
from collections import defaultdict

class Solution:
    def waysToFillArray(self, queries):
        mod = 10 ** 9 + 7
        #min factor number
        sfn = [0] * 10002
        for i in range(1, len(sfn)):
            # for prime i is factor number is i
            sfn[i] = i
        i = 2
        # till i * i
        while (i * i) <= 10001:
            # if i is prime:
            if sfn[i] == i:
                # start from i ^2
                j = i * i
                while j <= 10001:
                    if sfn[j] == j:
                        # set up its min factor is i
                        sfn[j] = i
                    j += i
            i += 1
        # pre-calculate n choose k
        choose = [[0] * 14 for _ in range(10033)]
        # i == 1 and 0 bukets is 1
        for i in range(len(choose)):
            choose[i][0] = 1
        for i in range(1, len(choose)):
            for j in range(1, len(choose[0])):
                # (n,k) = (n-1,k-1) + (n-1, k)
                choose[i][j] = (choose[i-1][j-1] + choose[i-1][j]) % mod
        # find factor frequenceis for [2,2,1,3,3] it returns [2,1,3]
        def get_factor_freq(x):
            fact_to_freq = defaultdict(int)
            while x > 1:
                fact_to_freq[sfn[x]] += 1
                # divie by factor
                x = x // sfn[x]
            return [f for f in fact_to_freq.values()]

        res = []
        for n,k in queries:
            # get factor frequencies
            frq = get_factor_freq(k)
            cur = 1
            # every l freqiency make h1 subsets and to get total number we multiply number subsets.
            # use stars and bars method to get number subsets for f factors:
            # f is non-distingushible number to needs to distribute in n buckets.
            # (f + n - 1) choose n
            for f in frq:
                cur = (cur * choose[n + f - 1][f]) % mod
            res.append(cur)
        return res

sol = Solution()
print(sol.waysToFillArray([[2,6],[5,1],[73,660]]))#4,1,50734910]

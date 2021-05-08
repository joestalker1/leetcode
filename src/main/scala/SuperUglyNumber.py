from heapq import heappop,heappush

class Solution:
    def nthSuperUglyNumber(self, n, primes) -> int:
        ugly = [0] * n
        ugly[0] = 1
        q = []
        # put minimal heap with val, index of last ugly, prime
        for i in range(len(primes)):
            heappush(q, (primes[i], 1, primes[i]))

        for i in range(1, n):
            #take min val
            a,_,_ = q[0]
            ugly[i] = a
            # until last ugly equals heap top
            while q[0][0] == ugly[i]:
                # val,idx, p
                val,idx,p = heappop(q)
                #multiply every prime on ugly[1...n] and increase index
                heappush(q, (p * ugly[idx], idx + 1, p))
        return ugly[-1]


sol = Solution()
#[1,2,4,7,8,13,14,16,19,26,28,32]
print(sol.nthSuperUglyNumber(100000, [7,19,29,37,41,47,53,59,61,79,83,89,101,103,109,127,131,137,139,157,167,179,181,199,211,229,233,239,241,251]))
print(sol.nthSuperUglyNumber(n = 12, primes = [2,7,13,19]))#32


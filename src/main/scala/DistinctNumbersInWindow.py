from collections import defaultdict


class Solution:
    def dNums(self, A, B):
        if not A or not B:
            return []
        wind = defaultdict(int)
        for i in range(B):
            wind[A[i]] += 1
        cnt = [len(wind)]
        for i in range(1,len(A) - B + 1):
            j = i + B - 1
            wind[A[i - 1]] -= 1
            wind[A[j]] += 1
            if wind[A[i-1]] == 0:
               del wind[A[i-1]]
            cnt.append(len(wind))
        return cnt

sol = Solution()
print(sol.dNums(A = [1, 2, 1, 3, 4, 3], B = 3))#[2, 3, 3, 2]
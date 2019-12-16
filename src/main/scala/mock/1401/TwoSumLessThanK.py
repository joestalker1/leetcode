from _collections import defaultdict

class Solution:
    def twoSumLessThanK(self, A, K):
        if not A or K == 0:
            return -1
        m = defaultdict(list)
        for i,a in enumerate(A):
            m[a].append(i)
        A.sort()
        p1 = 0
        p2 = len(A) - 1
        max_s = -1
        while p1 < p2:
            sum_of_2 = A[p1] + A[p2]
            if sum_of_2 > K:
                p2 -=1
            elif sum_of_2 == K:
                p1 += 1
                p2 -= 1
            else:
                max_s = max(max_s, sum_of_2)
                p1 += 1
        return max_s


sol = Solution()
print(sol.twoSumLessThanK([34,23,1,24,75,33,54,8], 60))
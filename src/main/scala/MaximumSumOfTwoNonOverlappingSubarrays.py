class Solution:
    def maxSumTwoNoOverlap2(self, A, L, M):
        prefix = [0] * len(A)
        prefix[0] = A[0]
        for i in range(1, len(A)):
            prefix[i] = prefix[i - 1] + A[i]
        l_max = prefix[L - 1]
        m_max = prefix[M - 1]
        max_sum = prefix[L + M - 1]
        for i in range(L + M, len(A)):
            # L,M
            l_max = max(l_max, prefix[i - M] - prefix[i - L - M])
            # M,L
            m_max = max(m_max, prefix[i - L] - prefix[i - L - M])
            max_sum = max(max_sum, l_max + prefix[i] - prefix[i - M], m_max + prefix[i] - prefix[i - L])
        return max_sum


sol = Solution()
print(sol.maxSumTwoNoOverlap(A=[0, 6, 5, 2, 2, 5, 1, 9, 4], L=1, M=2))
print(sol.maxSumTwoNoOverlap2(A=[0, 6, 5, 2, 2, 5, 1, 9, 4], L=1, M=2))
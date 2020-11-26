class Solution:
    def minSwap(self, A, B):
        swap1 = 1
        norm1 = 0
        for i in range(1, len(A)):
            swap2 = float('inf')
            norm2 = float('inf')
            if A[i - 1] < A[i] and B[i - 1] < B[i]:
                # could swap both A[i] and B[i]
                # don't swap on i - 1 and i
                norm2 = min(norm2, norm1)
                # swap on i - 1 and i
                swap2 = min(swap2, swap1 + 1)
            if A[i - 1] < B[i] and B[i - 1] < A[i]:
                # could swap either i-1 or i
                # don't swap on i but swap i - 1
                norm2 = min(norm2, swap1)
                # don't swap on i - 1 but swap on i
                swap2 = min(swap2, norm1 + 1)
            norm1 = norm2
            swap1 = swap2
        return min(norm1, swap1)


sol = Solution()
print(sol.minSwap([0, 3, 4, 5, 9, 10, 13, 16, 19, 24, 22, 24, 28, 28, 31, 32, 33, 34, 36, 38],
                  [0, 2, 4, 11, 13, 16, 17, 19, 23, 20, 25, 26, 27, 30, 30, 31, 33, 36, 37, 38]))
print(sol.minSwap([0, 4, 4, 5, 9], [0, 1, 6, 8, 10]))

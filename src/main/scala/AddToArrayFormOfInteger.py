class Solution(object):
    def addToArrayForm(self, A, K):
        A[-1] += K
        for i in range(len(A) - 1, -1, -1):
            carry, A[i] = divmod(A[i], 10)
            if i:
                A[i-1] += carry
        if carry:
            A.insert(0, carry)
        return A


sol = Solution()
print(sol.addToArrayForm(A = [2,1,5], K = 806))
print(sol.addToArrayForm(A = [1,2,0,0], K = 34))


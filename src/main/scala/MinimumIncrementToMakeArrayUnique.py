class Solution:
    def minIncrementForUnique(self, A):
        if not A or len(set(A)) == len(A):
            return 0
        A = sorted(A)
        moves = 0
        max_so_far = A[0]
        for i in range(1, len(A)):
            if A[i] <= max_so_far:
                moves += (max_so_far + 1 - A[i])
                A[i] = max_so_far + 1
            max_so_far = max(max_so_far, A[i])
        return moves


sol = Solution()
print(sol.minIncrementForUnique([3,2,1,2,1,7]))
print(sol.minIncrementForUnique([1,2,2]))







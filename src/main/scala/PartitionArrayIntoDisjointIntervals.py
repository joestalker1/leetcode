class Solution:
    def partitionDisjoint(self, A):
        minRight = [0] * len(A)
        maxLeft = [0] * len(A)

        m = A[-1]
        for i in range(len(A) - 1, -1, -1):
            m = min(m, A[i])
            minRight[i] = m

        m = A[0]
        for i in range(len(A)):
            m = max(m, A[i])
            maxLeft[i] = m

        for i in range(1, len(A)):
            if maxLeft[i - 1] <= minRight[i]:
                return i


sol = Solution()
print(sol.partitionDisjoint([32,57,24,19,0,24,49,67,87,87]))#7
print(sol.partitionDisjoint([1,1,1,0,6,12]))#4
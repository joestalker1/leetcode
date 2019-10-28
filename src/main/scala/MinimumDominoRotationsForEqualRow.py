class Solution(object):
    def minDominoRotations(self, A, B):
        if not A or not B:
            return -1

        def check(x):
            flip_a = 0
            flip_b = 0
            for i in range(len(A)):
                if A[i] != x and B[i] != x:
                    return -1
                if A[i] == x and B[i] != x:
                    flip_b += 1
                elif B[i] == x and A[i] != x:
                    flip_a += 1
            return min(flip_a, flip_b)
        flip = check(A[0])
        if flip == -1:
            return check(B[0])
        return flip

sol = Solution()
#print(sol.minDominoRotations(A = [3,5,1,2,3], B = [3,6,3,3,4]))
print(sol.minDominoRotations( A = [2,1,2,4,2,2], B = [5,2,6,2,3,2]))




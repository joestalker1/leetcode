class Solution:
    def validMountainArray(self, A):
        if len(A) < 3:
            return False
        # find peak
        peak = None
        for i in range(len(A) - 2):
            if A[i] < A[i+1] > A[i+2]:
                peak = i + 1
                break
        if not peak:
            return False
        for j in range(peak, len(A) - 1):
            if A[j] >= A[j+1]:
                return False
        return True


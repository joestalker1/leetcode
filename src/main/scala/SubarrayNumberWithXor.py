from collections import defaultdict

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        seq_xor = defaultdict(int)
        cnt = 0
        cur_xor = 0
        for i in range(len(A)):
            cur_xor ^= A[i]
            prev_xor = B ^ cur_xor
            if prev_xor in seq_xor:
                cnt += seq_xor[prev_xor]
            if cur_xor == B:
                cnt += 1
            seq_xor[cur_xor] += 1
        return cnt

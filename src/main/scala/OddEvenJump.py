class Solution(object):
    def oddEvenJumps(self, A):
        N = len(A)

        def next_jumps(indexes):
            # build monotonic stack
            next_jump = [None] * N
            stack = []  # invariant: stack is decreasing [4,3,2,2,1... <- top
            for i in indexes:
                while stack and i > stack[-1]: # i <= stack.top by keeping decreasing order
                    # if index is smaller, store it.
                    next_jump[stack.pop()] = i
                stack.append(i)
            return next_jump
        # sorted A in increasing order using indexes
        indexes = sorted(range(N), key=lambda i: A[i])
        # there is jump where we jump from i in oddnext
        oddnext = next_jumps(indexes)
        # sort in decreasin order
        indexes.sort(key=lambda i: -A[i])
        evennext = next_jumps(indexes)

        # for even and odd jumps: it true it can jump to i
        odd = [False] * N
        even = [False] * N
        odd[N - 1] = even[N - 1] = True
        # go from right to left
        for i in range(N - 2, -1, -1):
            # if we can jump from i, there even -> odd
            if oddnext[i] is not None:
                odd[i] = even[oddnext[i]]
            # jump from odd to even
            if evennext[i] is not None:
                even[i] = odd[evennext[i]]
        # count number of True(1)
        return sum(odd)


sol = Solution()
print(sol.oddEvenJumps([10,13,12,14,15]))
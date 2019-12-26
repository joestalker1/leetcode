class Solution:
    def buddyStrings(self, A, B):
        if not A and not B:
            return False
        if not A or not B:
            return False
        A = list(A)
        B = list(B)
        if A == B:
            chars = set()
            for char in A:
                if char in chars:
                    return True
                chars.add(char)
            return False
        else:
            res = []
            for i in range(len(A)):
                if A[i] != B[i]:
                    res.append(i)
            if len(res) != 2:
                return False
            i,j = res[0],res[1]
            return A[i] == B[j] and A[j] == B[i]

sol = Solution()
print(sol.buddyStrings("ab", "ab"))
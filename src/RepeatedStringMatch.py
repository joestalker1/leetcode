class Solution:
    def repeatedStringMatch(self, A, B):
        q = (len(B) - 1) // len(A) + 1
        for i in range(2):
            s = A*(q+i)
            if B in s:
                return q + i
        return -1

sol = Solution()
print(sol.repeatedStringMatch("abababaaba", "aabaaba"))
print(sol.repeatedStringMatch("abcd", "cdabcdab"))



class Solution:
    def minRepeats(self, A, B):
        # code here
        A = A.strip()
        B = B.strip()
        res = A
        c = 1
        while len(res) < len(B):
            c += 1
            res += A

        def is_substr(s, sub):
            n = len(s)
            m = len(sub)
            for i in range(n-m + 1):
                j = 0
                while j < m:
                    if s[i+j] != sub[j]:
                        break
                    j+=1
                if j == m:
                    return True
            return False
        if is_substr(res, B):
            return c
        res += A
        if is_substr(res, B):
            return c + 1
        return -1


sol = Solution()
#print(sol.minRepeats("", ""))
#print(sol.minRepeats("abcd", "cd"))#1
print(sol.minRepeats("abcd", "cdabcdab"))#3
print(sol.minRepeats("ab","cab"))
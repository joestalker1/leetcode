class Solution:
    def minCharacters(self, a, b):
        c1 = [0] * 26
        c2 = [0] * 26
        for ch in a:
            c1[ord(ch) - ord('a')] += 1
        for ch in b:
            c2[ord(ch) - ord('a')] += 1
        m = len(a)
        n = len(b)
        res = m + n
        for i in range(26):
            # how many need to make a and b with one distinct char
            res = min(res, m + n - c1[i] - c2[i])
            if i > 0:
                c1[i] += c1[i - 1]
                c2[i] += c2[i - 1]
            if i < 25:
                res = min(res, m - c1[i] + c2[i], n - c2[i] + c1[i])
        return res


sol = Solution()
print(sol.minCharacters("aaa", "aab"))#1
print(sol.minCharacters("dee", "a"))#0
print(sol.minCharacters("a", "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"))#2
print(sol.minCharacters("bddae", "abbb"))#2
print(sol.minCharacters("c", "d"))#0
print(sol.minCharacters("aaa", "ccc"))#0
print(sol.minCharacters("aba", "caa"))#2
print(sol.minCharacters("dabadd", "cda"))  # 3

class Solution:
    def countAndSay(self, n):
        if n < 1:
            return n
        s = '1'
        i = 2
        while i <= n:
            j = 0
            sn = ''
            while j < len(s):
                ch = s[j]
                k = 1
                j += 1
                while j < len(s) and ch == s[j]:
                    k += 1
                    j += 1
                sn = sn + str(k) + ch
            s = sn
            i += 1
        return s

sol = Solution()
print(sol.countAndSay(4))


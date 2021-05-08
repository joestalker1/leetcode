class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)
        #is polindrom for i to j
        pol = [[False] * n for _ in range(n)]
        #cut from i to n-1
        d = [0] * n
        for i in range(n-1, -1, -1):
            d[i] = n - i - 1
            #consider every j position as cut point,
            #and s[i:j],s[i:j+1],s[i:j+2] and so on by updating d[i] if i:j is polindrom and [i+1:j-1], it may decrease cut number
            # we go from right to left, so we have cuts calculated for rightmost.
            for j in range(i, n):
                if s[i] == s[j] and (j - i < 2 or pol[i+1][j-1]):
                    pol[i][j] = True
                    if j == n - 1:
                        d[i] = 0
                    # if s[j+1:n-1] has d[j+1] cuts and if d[j+1] + 1(s[i:j] is polindrom),then update d
                    elif d[j + 1] + 1 < d[i]:
                        d[i] = d[j + 1] + 1
        return d[0]

sol = Solution()
#print(sol.minCut("apjesgpsxoeiokmqmfgvjslcjukbqxpsobyhjpbgdfruqdkeiszrlmtwgfxyfostpqczidfljwfbbrflkgdvtytbgqalguewnhvvmcgxboycffopmtmhtfizxkmeftcucxpobxmelmjtuzigsxnncxpaibgpuijwhankxbplpyejxmrrjgeoevqozwdtgospohznkoyzocjlracchjqnggbfeebmuvbicbvmpuleywrpzwsihivnrwtxcukwplgtobhgxukwrdlszfaiqxwjvrgxnsveedxseeyeykarqnjrtlaliyudpacctzizcftjlunlgnfwcqqxcqikocqffsjyurzwysfjmswvhbrmshjuzsgpwyubtfbnwajuvrfhlccvfwhxfqthkcwhatktymgxostjlztwdxritygbrbibdgkezvzajizxasjnrcjwzdfvdnwwqeyumkamhzoqhnqjfzwzbixclcxqrtniznemxeahfozp"))
#print(sol.minCut("ab"))
print(sol.minCut("leet"))
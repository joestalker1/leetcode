class Solution:
    def minWindow(self, S, T):
        if not S and not T or len(T) > len(S):
            return ""
        dp = [i if S[i] == T[0] else -1 for i in range(len(S))]
        left = -1
        for i in range(len(T)):
            k = -1
            new = [-1] * len(S)
            for j in range(left + 1, len(S)):
                if S[j] == T[i]:
                    if i == 0:
                        new[j] = j
                    else:
                        new[j] = dp[j - 1]
                    if k == -1:
                        k = j
                elif j > 0:
                    new[j] = new[j - 1]
            if k != -1:
                left = k
            dp = new
        res = [0, float('inf')]
        for j in range(0, len(S)):
            if dp[j] > -1:
                s, e = dp[j], j
                if res[1] - res[0] > e - s:
                    res = [s, e]
        return S[res[0]:res[1] + 1] if res[1] != float('inf') else ''


sol = Solution()
print(sol.minWindow(
    "ffynmlzesdshlvugsigobutgaetsnjlizvqjdpccdylclqcbghhixpjihximvhapymfkjxyyxfwvsfyctmhwmfjyjidnfryiyajmtakisaxwglwpqaxaicuprrvxybzdxunypzofhpclqiybgniqzsdeqwrdsfjyfkgmejxfqjkmukvgygafwokeoeglanevavyrpduigitmrimtaslzboauwbluvlfqquocxrzrbvvplsivujojscytmeyjolvvyzwizpuhejsdzkfwgqdbwinkxqypaphktonqwwanapouqyjdbptqfowhemsnsl",
    "ntimcimzah"))  # "nevavyrpduigitmrimtaslzboauwbluvlfqquocxrzrbvvplsivujojscytmeyjolvvyzwizpuhejsdzkfwgqdbwinkxqypaph"
#
# print(sol.minWindow("cnhczmccqouqadqtmjjzl", "cm"))  # czm
# print(sol.minWindow(
#     "ffynmlzesdshlvugsigobutgaetsnjlizvqjdpccdylclqcbghhixpjihximvhapymfkjxyyxfwvsfyctmhwmfjyjidnfryiyajmtakisaxwglwpqaxaicuprrvxybzdxunypzofhpclqiybgniqzsdeqwrdsfjyfkgmejxfqjkmukvgygafwokeoeglanevavyrpduigitmrimtaslzboauwbluvlfqquocxrzrbvvplsivujojscytmeyjolvvyzwizpuhejsdzkfwgqdbwinkxqypaphktonqwwanapouqyjdbptqfowhemsnsl",
#     "michmznait"))
# print(sol.minWindow("fgrqsqsnodwmxzkzxwqegkndaa", "kzed"))  # "kzxwqegknd"
# print(sol.minWindow("hpsrhgogezyfrwfrejytjkzvgpjnqil", "sgy"))  # srhgogezy
print(sol.minWindow("cnhczmccqouqadqtmjjzl", "dq"))  # dq
print(sol.minWindow(S="abcdebdde", T="bde"))  # bcde

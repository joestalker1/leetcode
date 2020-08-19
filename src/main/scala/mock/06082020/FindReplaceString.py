class Solution:
    def findReplaceString(self, S: str, indexes, sources, targets):
        if not S:
            return S
        res = []
        for i in range(len(indexes)):
            ind = indexes[i]
            src = sources[i]
            dest = targets[i]
            if S[ind:ind + len(src)] == src:
                res.append([ind, dest, len(src)])
        res.sort(key=lambda x: x[0])
        T = []
        for i in range(len(res) - 1):
            cur_end = res[i][0] + res[i][2]-1
            next_start = res[i + 1][0]
            T.append(res[i][1])
            if cur_end + 1 < next_start:
                T.append(S[res[i][0] + res[i][2]:next_start])
        T.append(res[-1][1])
        return ''.join(T)

sol = Solution()
print(sol.findReplaceString("abcd",[0, 2], ["a", "cd"], ["eee", "ffff"]))#"eeebffff"









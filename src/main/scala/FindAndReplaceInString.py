class Solution:
    def findReplaceString(self, S: str, indexes, sources, targets):
        if not S:
            return S
        res = []
        # s has src substring,append replacement to res
        for i in range(len(indexes)):
            ind = indexes[i]
            src = sources[i]
            dest = targets[i]
            if S[ind:ind + len(src)] == src:
                res.append([ind, ind + len(src), dest])
        if not res:
            return S
        res.sort(key=lambda x: x[0])
        new_res = []
        start = 0
        for s1, e1, dest in res:
            end = s1
            new_res.append(S[start:end])
            new_res.append(dest)
            start = e1

        new_res.append(S[start:])
        return ''.join(new_res)
class Solution:
    def partitionLabels(self, S):
        if not S:
            return []
        last = {c: i for i,c in enumerate(S)}
        j,start = 0,0
        res = []
        for i in range(len(S)):
            j = max(j, last[S[i]])
            if i == j:
                res.append(i - start + 1)
                start = i + 1
        return res



sol = Solution()
print(sol.partitionLabels("ababcbacadefegdehijhklij"))
        
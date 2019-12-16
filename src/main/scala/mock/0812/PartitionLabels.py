class Solution:
    def partitionLabels(self, s):
        if not s:
            return []
        m = {c:i for i,c in enumerate(s)}
        parts = []
        j = 0
        max_i = 0
        last = 0
        while j < len(s):
            max_i = max(max_i, m[s[j]])
            if j == max_i:
                parts.append(j - last + 1)
                last = j + 1
            j += 1
        return parts


sol = Solution()
print(sol.partitionLabels("ababcbacadefegdehijhklij"))








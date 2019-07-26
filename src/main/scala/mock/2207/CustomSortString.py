from collections import Counter

class Solution:
    def customSortString(self, S, T):
        if not S or not T:
            return
        chars = Counter(T)
        res = []
        for ch in S:
            res.append(ch * chars[ch])
            chars[ch] = 0
        for ch,count in chars.items():
            res.append(ch * count)
        return ''.join(res)


sol = Solution()
print(sol.customSortString("cba", "abcd"))
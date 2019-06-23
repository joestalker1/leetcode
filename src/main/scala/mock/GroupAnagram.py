class Solution:
    def groupAnagrams(self, strs):
        if not strs:
            return []
        res = {}
        for i in range(len(strs)):
            chars = sorted(strs[i])
            k = ''.join(chars)
            if k not in res:
                res[k] = []
            res[k].append(strs[i])
        return res.values()


sol = Solution()
print(sol.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))






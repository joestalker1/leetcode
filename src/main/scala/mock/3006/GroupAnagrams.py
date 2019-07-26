class Solution(object):
    def groupAnagrams(self, words):
        if not words:
            return []
        res = {}
        for i in range(len(words)):
            key = ''.join(sorted(words[i]))
            if key not in res:
                res[key] = []
            res[key].append(words[i])
        return list(res.values())


sol = Solution()
print(sol.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))


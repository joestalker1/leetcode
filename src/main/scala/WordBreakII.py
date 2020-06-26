from collections import defaultdict


class Solution:
    def wordBreak(self, s: str, wordDict):
        if not s and not wordDict:
            return True
        if not s or not wordDict:
            return False

        wordDict = set(wordDict)
        found = defaultdict(list)
        dp = [False] * (len(s) + 1)
        dp[0] = True
        for l in range(1, len(s) + 1):
            for i in range(l):
                if dp[i]:
                    w = s[i:l]
                    if w in wordDict:
                        found[i].append(w)
                        dp[l] = True

        if not dp[-1]:
            return False

        def dfs(words, i, res, buf):
            if i == len(s):
                res.append(' '.join(buf))
                return

            for w in words[i]:
                buf.append(w)
                dfs(words, i + len(w), res, buf)
                buf.pop(-1)

        res = []
        dfs(found, 0, res, [])
        return res


sol = Solution()
print(sol.wordBreak("catsanddog", ["cat", "cats", "and", "sand", "dog"]))

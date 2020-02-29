class Solution:
    def smallestSubsequence(self, text):
        chars = [0] * 26
        for i,c in enumerate(text):
            chars[ord(c) - ord('a')] = i
        res = []
        seen = set()
        for i,c in enumerate(text):
            if c in seen:
                continue
            while len(res) and res[-1] > c and chars[ord(res[-1]) - ord('a')] > i:
                res.pop()
            seen.add(c)
            res.append(c)
        return ''.join(res)


sol = Solution()
print(sol.smallestSubsequence("leetcode"))  # "letcod"
print(sol.smallestSubsequence("cdadabcc"))

from collections import defaultdict
import re
class Solution:
    def mostCommonWord(self, paragraph, banned):
        if not paragraph:
            return []
        words = re.split("[!?',;. ]", paragraph.lower())
        freq = defaultdict(lambda :0)
        banned = set(banned)
        for word in words:
            if not word:
                continue
            if word not in banned:
                freq[word] += 1
        best,res = 0, ''
        for w,f in freq.items():
            if f > best:
                best = f
                res = w
        return res


sol = Solution()
print(sol.mostCommonWord("Bob hit a ball, the hit BALL flew far after it was hit.", ["hit"]))


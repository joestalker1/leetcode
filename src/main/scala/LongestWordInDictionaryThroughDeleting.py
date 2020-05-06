from collections import defaultdict
from bisect import bisect_right


class Solution:
    def findLongestWord(self, s, d):
        char_to_pos = defaultdict(list)
        for i, ch in enumerate(s):
            char_to_pos[ch].append(i)
        d.sort(key=lambda w: len(w), reverse=True)
        for word in d:
            found = False
            last_j = -1
            for i in range(len(word)):
                if word[i] not in char_to_pos:
                    found = False
                    break
                j = bisect_right(char_to_pos[word[i]], last_j, 0, len(char_to_pos[word[i]]) - 1)
                x = char_to_pos[word[i]][j]
                if x <= last_j:
                    found = False
                    break
                last_j = x
                found = True

            if found:
                return word
        return ''


sol = Solution()
print(sol.findLongestWord(s="abpcplea", d=["ale", "apple", "monkey", "plea"]))
print(sol.findLongestWord("abpcplea", ["aaa", "b", "c"]))

import bisect
from collections import defaultdict

class Solution:
    def numMatchingSubseq(self, s: str, words) -> int:
        if not s or not words:
            return 0

        def is_subseq(char_to_pos, word):
            if len(word) > len(s):
                return False
            j = 0
            for ch in word:
                if len(char_to_pos[ch]) == 0 or j == len(s):
                    return False
                k = bisect.bisect_right(char_to_pos[ch], j)
                if k == len(char_to_pos[ch]):
                    k -= 1
                if char_to_pos[ch][k] < j:
                    return False
                if k > 0 and char_to_pos[ch][k - 1] == j:
                    j = char_to_pos[ch][k - 1] + 1
                else:
                    j = char_to_pos[ch][k] + 1
            return True

        char_to_pos = defaultdict(list)
        for i, ch in enumerate(s):
            char_to_pos[ch].append(i)
        cnt = 0
        for word in words:
            if is_subseq(char_to_pos, word):
                cnt += 1
        return cnt
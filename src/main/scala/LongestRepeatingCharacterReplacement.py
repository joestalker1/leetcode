from collections import defaultdict


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_len = 0
        max_chars = 0
        chars = defaultdict(int)
        b = 0
        for e in range(len(s)):
            ch = s[e]
            chars[ch] += 1
            max_chars = max(chars[ch], max_chars)

            while e - b - max_chars + 1 > k:
                ch = s[b]
                chars[ch] -= 1
                b += 1
            max_len = max(max_len, e - b + 1)
        return max_len

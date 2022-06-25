from collections import defaultdict

class Solution:
    def maxProduct(self, words) -> int:
        if not words:
            return 0
        code = lambda ch: ord(ch) - ord('a')
        bit_mask = defaultdict(int)
        for word in words:
            mask = 0
            for ch in word:
                mask |= (1 << code(ch))
            bit_mask[mask] = max(len(word), bit_mask[mask])
        max_prod = 0
        for word1 in bit_mask:
            for word2 in bit_mask:
                if word1 & word2 == 0:
                    max_prod = max(max_prod, bit_mask[word1]*bit_mask[word2])
        return max_prod
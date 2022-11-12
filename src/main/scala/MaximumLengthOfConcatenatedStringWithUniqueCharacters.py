class Solution:
    def maxLength(self, arr) -> int:
        if not arr:
            return 0

        def word_to_bitset(bitset, word):
            res = 0
            for ch in word:
                mask = 1 << (ord(ch) - ord('a'))
                if mask & res:
                    return
                res += mask
            bitset.append(res + (len(word) << 26))

        def find_max_len(bitset, i, res):
            prev_chars = res & ((1 << 26) - 1)
            prev_len = res >> 26
            max_len = prev_len
            for j in range(i, len(bitset)):
                cur_chars = bitset[j] & ((1 << 26) - 1)
                cur_len = bitset[j] >> 26
                if cur_chars & prev_chars:
                    continue
                new_chars = cur_chars + prev_chars + ((prev_len + cur_len) << 26)
                max_len = max(max_len, find_max_len(bitset, j + 1, new_chars))
            return max_len

        bitset = []
        for word in arr:
            word_to_bitset(bitset, word)

        return find_max_len(bitset, 0, 0)
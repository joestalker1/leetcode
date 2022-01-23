from collections import defaultdict

class Solution:
    def wonderfulSubstrings(self, word: str) -> int:
        # assert self._wonderfulSubstrings('abc') == 6,'test1'
        # assert self._wonderfulSubstrings('aa') == 3, 'test2'
        # assert self._wonderfulSubstrings('aba') == 4, 'test3'
        return self._wonderfulSubstrings(word)

    def _wonderfulSubstrings(self, word: str) -> int:
        pr = defaultdict(int)
        pr[0] = 1

        def get_hash(ch):
            return 1 << (ord(ch) - ord('a'))

        cur = 0
        string = 0
        chars = set()
        for ch in word:
            cur ^= get_hash(ch)
            chars.add(ch)
            for c in chars:
                string += pr[cur ^ get_hash(c)]
            string += pr[cur]
            pr[cur] += 1
        return string

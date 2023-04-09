class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        # assert self._numberOfSubstrings('aaa') == 0, 'test1'
        # assert self._numberOfSubstrings('abc') == 1, 'test2'
        # assert self._numberOfSubstrings('abcabc') == 10, 'test3'
        # assert self._numberOfSubstrings('aaacb') == 3, 'test4'
        # assert self._numberOfSubstrings('acbbcac') == 11, 'test5'
        return self._numberOfSubstrings(s)

    def _numberOfSubstrings(self, s: str) -> int:
        if not s:
            return 0
        substr_cnt = 0
        need_chars = {'a':0,'b':0,'c':0}
        #number of substring number with a,b,c
        k = 0
        for i,ch in enumerate(s):
            if ch in need_chars:
                need_chars[ch] += 1
                while need_chars['a'] and need_chars['b'] and need_chars['c']:
                    if s[k] in need_chars:
                        need_chars[s[k]] -= 1
                    k += 1
            substr_cnt += k
        return substr_cnt
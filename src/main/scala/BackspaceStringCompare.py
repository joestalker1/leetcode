import itertools


class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        if not S and not T:
            return True
        if not S or not T:
            return False

        def iter_with_bs(s):
            i = len(s) - 1
            skip = 0
            while i >= 0:
                if s[i] == '#':
                    skip += 1
                elif skip:
                    skip -= 1
                else:
                    yield s[i]
                i -= 1

        return all(ch1 == ch2 for ch1, ch2 in itertools.zip_longest(iter_with_bs(S), iter_with_bs(T)))
import itertools


class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        if not S and not T:
            return True
        if not S or not T:
            return False

        def process(s):
            skip = 0
            for ch in reversed(s):
                if ch == '#':
                    skip += 1
                elif skip:
                    skip -= 1
                else:
                    yield ch
        # iterate until longest iterable is exhausted by replacing shortes char with None
        return all(a == b for a, b in itertools.zip_longest(process(S), process(T)))
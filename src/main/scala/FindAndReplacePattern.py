class Solution:
    def findAndReplacePattern(self, words, pattern: str):
        if not words or not pattern:
            return []

        def match(word):
            m = {}
            for w, p in zip(word, pattern):
                if m.setdefault(w, p) != p:
                    return False
            return len(set(m.values())) == len(m.values())

        return filter(match, words)
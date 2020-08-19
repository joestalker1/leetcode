class AutocompleteSystem:

    def __init__(self, sentences, times):
        self.chars = {}
        for sentence, time in zip(sentences, times):
            self.add(sentence, time)
        self.buf = []

    def add(self, words, times):
        p = self.chars
        for i in range(len(words)):
            ch = words[i]
            p.setdefault(ch, {})
            p = p[ch]
        p['#'] = times

    def update(self, words, times):
        p = self.chars
        for i in range(len(words)):
            ch = words[i]
            p = p[ch]
        p['#'] += times

    def traverse(self, s, p, res):
        if '#' in p:
            res.append([s, p['#']])

        for ch in p.keys():
            if ch != '#':
                self.traverse(s + ch, p[ch], res)

    def search(self, s):
        p = self.chars
        res = []
        for ch in s:
            if ch not in p:
                return res
            p = p[ch]
        self.traverse(s, p, res)
        return res

    def has(self, words):
        p = self.chars
        for i in range(len(words)):
            ch = words[i]
            if ch not in p:
                return False
            p = p[ch]
        return '#' in p

    def input(self, c):
        if c == '#':
            words = ''.join(self.buf)
            self.buf = []

            if self.has(words):
                self.update(words, 1)
            else:
                self.add(words, 1)
            return []
        self.buf.append(c)
        words = ''.join(self.buf)
        candidates = self.search(words)
        if candidates:
            candidates.sort(key=lambda x: (-x[1], x[0]))
            return [s for s, t in candidates[:3]]
        return []


# ["AutocompleteSystem","input","input","input","input","input","input","input","input","input","input","input","input","input","input"]
# [[["abc","abbc","a"],[3,3,3]],["b"],["c"],["#"],["b"],["c"],["#"],["a"],["b"],["c"],["#"],["a"],["b"],["c"],["#"]]

# [null,[],[],[],["bc"],["bc"],[],["a","abbc","abc"],["abbc","abc"],["abc"],[],["abc","a","abbc"],["abc","abbc"],["abc"],[]]

acs = AutocompleteSystem(["abc", "abbc", "a"], [3, 3, 3])
print(acs.input('b'))
print(acs.input('c'))
print(acs.input('#'))

print(acs.input('b'))
print(acs.input('c'))
print(acs.input('#'))

print(acs.input('a'))
print(acs.input('b'))
print(acs.input('c'))
print(acs.input('#'))

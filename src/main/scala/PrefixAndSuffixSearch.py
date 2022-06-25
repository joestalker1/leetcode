import collections

Trie = lambda: collections.defaultdict(Trie)
W = 0

class WordFilter:
    def __init__(self, words):
        self.trie = Trie()
        for w,word in enumerate(words):
            word += '#'
            for i in range(len(word)):
                cur = self.trie
                cur[W] = w
                for j in range(i,2*len(word)-1):
                    cur = cur[word[j % len(word)]]
                    cur[W] = w

    def f(self, prefix: str, suffix: str) -> int:
        cur = self.trie
        for let in suffix+'#'+prefix:
            if let not in cur:
                return -1
            cur = cur[let]
        return cur[W]
class TrieNode:
    def __init__(self,ch):
        self.ch = ch
        self.term = False
        self.children = [None] * 27


class Trie:
    def __init__(self):
        self.root = TrieNode('')

    def index(self, a):
        return ord(a) - ord('a')

    def insert(self, word):
        i = 0
        p = self.root
        while i < len(word):
            ch = word[i]
            if not p.children[self.index(ch)]:
                p.children[self.index(ch)] = TrieNode(ch)
            p = p.children[self.index(ch)]
            i += 1
        p.term = True

    def traverse(self, p, word):
        i = 0
        while i < len(word):
            ch = word[i]
            if p.ch != ch or i + 1 < len(word) and not p.children[self.index(word[i + 1])]:
                return None
            if i + 1 < len(word):
                p = p.children[self.index(word[i + 1])]
            i += 1
        return p

    def search(self, word):
        if not self.root.children[self.index(word[0])]:
            return False
        n = self.traverse(self.root.children[self.index(word[0])], word)
        if not n:
            return False
        return n.term

    def startsWith(self, prefix):
        if not self.root.children[self.index(prefix[0])]:
            return False
        n = self.traverse(self.root.children[self.index(prefix[0])], prefix)
        return n is not None


trie = Trie()
trie.insert("apple")
print(trie.search("app"))
print(trie.startsWith("app"))
trie.insert("app")
print(trie.search("app"))


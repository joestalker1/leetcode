class Trie:
    def __init__(self):
        self.chars = {}

    def add(self, word):
        cur = self.chars
        for ch in word:
            cur.setdefault(ch, {})
            cur = cur[ch]
        cur['#'] = '#'

    def find(self, word):

        cur = self.chars
        for ch in word:
            if ch not in cur:
                return False
            cur = cur[ch]
        return '#' in cur


class StreamChecker:
    def __init__(self, words):
        self.trie = Trie()
        for word in words:
            self.trie.add(word)
        self.word_lens = [len(word) for word in words]
        self.buf = []

    def query(self, letter):
        self.buf.append(letter)
        for word_len in self.word_lens:
            if len(self.buf) < word_len:
                continue
            sub = self.buf[len(self.buf)-word_len:]
            if self.trie.find(''.join(sub)):
                return True
        return False

#["StreamChecker","query","query","query","query","query","query","query","query","query","query","query","query","query","query","query","query","query","query","query","query","query","query","query","query","query","query","query","query","query","query"]
#[[["ab","ba","aaab","abab","baa"]],["a"],["a"],["a"],["a"],["a"],["b"],["a"],["b"],["a"],["b"],["b"],["b"],["a"],["b"],["a"],["b"],["b"],["b"],["b"],["a"],["b"],["a"],["b"],["a"],["a"],["a"],["b"],["a"],["a"],["a"]]
#["StreamChecker","query","query","query","query","query","query","query","query","query","query","query","query"]
#[[["cd","f","kl"]],["a"],["b"],["c"],["d"],["e"],["f"],["g"],["h"],["i"],["j"],["k"],["l"]]
#             [null,false,false,false,true,false,true,false,false,false,false,false,true]
sc = StreamChecker(["cd","f","kl"])
print(sc.query("a"))
print(sc.query("b"))
print(sc.query("c"))
print(sc.query("d"))#true
print(sc.query("e"))
print(sc.query("f"))
print(sc.query("g"))
print(sc.query("h"))
print(sc.query("i"))
print(sc.query("j"))
sc.query("k")
sc.query("l")

# sc = StreamChecker(["ab","ba","aaab","abab","baa"])
# print(sc.query("a"))
# print(sc.query("a"))
# print(sc.query("a"))
# print(sc.query("a"))
# print(sc.query("a"))
# print(sc.query("b"))#true
# print(sc.query("a"))# true
# print(sc.query("b"))#true
# print(sc.query("a"))
# print(sc.query("b"))
class Trie:
    def __init__(self, sentences, times):
        self.chars = {}

    def add(self, words):
        p = self.chars
        for i in range(len(words)):
            ch = words[i]
            p.setdefault(ch, {})
            p = p[ch]
        p['#'] = '#'


    def find(self, words):
        p = self.chars
        for i in range(len(words)):
            ch = words[i]
            if ch not in p:
                return False
            p = p[ch]
        return '#' in p


class StreamChecker:

    def __init__(self, words):
        self.trie = Trie()
        self.words = words
        self.chars = set()
        for word in words:
            self.trie.add(word)

    def query(self, letter) -> bool:
        for i in range(len(letter)):
            for len_word in range(1, len(letter)):
                word = letter[i:i+len_word]
                if self.trie.find(word):
                    return True
        return False


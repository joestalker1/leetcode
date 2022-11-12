from collections import Counter


class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False


class StrNum:
    def __init__(self, k):
        self.k = k


class Trie:
    def __init__(self, k):
        self.node = TrieNode()
        self.need_str = k

    def add(self, word):
        cur = self.node
        for ch in word:
            if ch not in cur.children:
                cur.children[ch] = TrieNode()
            cur = cur.children[ch]
        cur.endOfWord = True

    def find(self):

        def find_words(cur, prefix):
            if self.need_str.k == 0:
                return []
            words = []
            if cur.endOfWord:
                self.need_str.k -= 1
                words.append(prefix)
            for i in range(26):
                ch = chr(ord('a') + i)
                if ch in cur.children:
                    words += find_words(cur.children[ch], prefix + ch)
            return words

        return find_words(self.node, '')


class Solution:
    def topKFrequent(self, words, k: int):
        n = len(words)
        freq = Counter(words)
        str_num = StrNum(k)
        bucket = [Trie(str_num) for _ in range(n + 1)]

        for word in freq:
            bucket[freq[word]].add(word)

        word_in_lex_order = []
        for frq in range(n - 1, 0, -1):
            if str_num.k == 0:
                return word_in_lex_order
            word_in_lex_order += bucket[frq].find()
        return word_in_lex_order
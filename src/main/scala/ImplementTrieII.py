class TrieNode:
    def __init__(self):
        self.ref_cnt = 0
        self.end_word_cnt = 0
        self.children = {}
        self.endOfWord = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        cur_node = self.root
        for ch in word:
            if ch not in cur_node.children:
                cur_node.children[ch] = TrieNode()
            cur_node = cur_node.children[ch]
            cur_node.ref_cnt += 1
        cur_node.endOfWord = True
        cur_node.end_word_cnt += 1

    def countWordsEqualTo(self, word):
        cur_node = self.root
        for ch in word:
            if ch not in cur_node.children:
                return 0
            cur_node = cur_node.children[ch]
        return cur_node.end_word_cnt

    def countWordsStartingWith(self, word):
        cur_node = self.root
        for ch in word:
            if ch not in cur_node.children:
                return 0
            cur_node = cur_node.children[ch]
        return cur_node.ref_cnt

    def erase(self, word):
        cur_node = self.root
        for ch in word:
            if ch not in cur_node.children:
                return
            cur_node = cur_node.children[ch]
            if cur_node.ref_cnt > 0:
                cur_node.ref_cnt -= 1
        if cur_node.end_word_cnt > 0:
            cur_node.end_word_cnt -= 1
        if cur_node.endOfWord and cur_node.end_word_cnt == 0:
            cur_node.endOfWord = False


trie = Trie()
trie.insert('abc')
trie.insert('abc')
trie.insert('abcd')
print(trie.countWordsEqualTo('abc'))
print(trie.countWordsEqualTo('abcd'))
trie.erase('abcd')
trie.erase('abcd')
print(trie.countWordsEqualTo('abcd'))
print(trie.countWordsEqualTo('abc'))


class TrieNode:
    def __init__(self):
        self.chars = {}
        self.cnt = 0


class Trie:
    def __init__(self):
        self.head = TrieNode()
        self.nodes = {}

    def add(self, i, s):
        cur = self.head
        for ch in s:
            if ch not in cur.chars:
                cur.chars[ch] = TrieNode()
                cur.cnt += 1
            cur = cur.chars[ch]
        self.nodes[cur] = i

    def uniq_node_index(self):
        uniq = []
        for node in self.nodes:
            if node.cnt == 0:
                uniq.append(self.nodes[node])
        return uniq


class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        if not words:
            return 0
        trie = Trie()
        for i in range(len(words)):
            trie.add(i, words[i][::-1])
        uniq_node_index = trie.uniq_node_index()
        cur_len = 0
        for i in uniq_node_index:
            cur_len += len(words[i]) + 1
        return cur_len

    
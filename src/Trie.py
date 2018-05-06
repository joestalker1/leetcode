class Node:
    def __init__(self,c):
        self.c = c
        self.children = {}
        self.end = 0


class Trie:
    def __init__(self):
        self.words = []
        self.root = Node('0')

    def insert(self, word, index):
        cur = self.root
        for ch in list(word):
            if ch not in cur.children:
                cur.children[ch] = Node(ch)
            cur = cur.children[ch]
        cur.end = index

    def dfs(self):
        ans = ""
        stack = list()
        stack.append(self.root)
        while len(stack) > 0:
            node = stack.pop()
            if node.end > 0 or node == self.root:
                if node != self.root:
                    word = self.words[node.end - 1]
                    if len(word) > len(ans) or len(word) == len(ans) and word < ans:
                        ans = word
                for nei in node.children.values():
                    stack.append(nei)

        return ans


class Solution:
    def longestWord(self, words):
        trie = Trie()
        index = 0
        for word in words:
            index += 1
            trie.insert(word, index)
        trie.words = words
        return trie.dfs()


sol = Solution()
print(sol.longestWord(["a", "banana", "app", "appl", "ap", "apply", "apple"]))
class Trie:
    def __init__(self):
        self.chars = {}

    def add(self, s):
        m = self.chars
        for ch in s:
            m = m.setdefault(ch, {})
        m['#'] = s


class Solution:
    def findWords(self, board, words):
        # if not words or not board:
        #     return []
        trie = Trie()
        for word in words:
            trie.add(word)

        def backtracking(r,c, parent, res):
            letter = board[r][c]
            curnode = parent[letter]
            if '#' in curnode:
                res.append(curnode['#'])
            board[r][c] = '{}'
            for dr, dc in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                r1 = r + dr
                c1 = c + dc
                if 0 <= r1 < len(board) and 0 <= c1 < len(board[0]):
                    ch = board[r1][c1]
                    if ch in curnode:
                        backtracking(r1, c1, curnode, res)
            board[r][c] = letter
            if '#' in curnode:
                curnode.pop('#')

        res = []
        for i in range(len(board)):
            for j in range(len(board[0])):
                ch = board[i][j]
                if ch in trie.chars:
                    backtracking(i, j, trie.chars, res)
        return res


sol = Solution()
#["ab","ac","bd","ca","db"]
print(sol.findWords([["a", "b"], ["c", "d"]],
                    ["ab", "cb", "ad", "bd", "ac", "ca", "da", "bc", "db", "adcb", "dabc", "abb", "acb"]))

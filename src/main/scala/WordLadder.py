class Solution:
    def dfs(self, beginWord, endWord, wordList, used, length):
        if beginWord == endWord or len(used) == len(wordList):
            return length
        min_len = len(wordList)
        for word in wordList:
            if word in used:
                continue
            if len(set(word) & set(beginWord)) == 2:
                used.add(word)
                min_len = min(min_len, self.dfs(word, endWord, wordList, used, length + 1))
                used.remove(word)
        return min_len

    def ladderLength(self, beginWord: 'str', endWord: 'str', wordList: 'List[str]') -> 'int':
        if not wordList or not beginWord or not endWord:
            return 0
        used = set()
        used.add(beginWord)
        used.add(endWord)
        return self.dfs(beginWord, endWord, wordList,used, 2)

sol = Solution()
print(sol.ladderLength("hit", "cog", ["hot","dot","dog","lot","log","cog"]))

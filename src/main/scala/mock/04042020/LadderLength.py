class Solution:
    def ladderLength(self, beginWord, endWord, wordList):
        if not beginWord or not endWord or not wordList:
            return 0

        def has_one_diff(word1, word2):
            diff_count = 0
            for i in range(len(word1)):
                if word1[i] != word2[i]:
                    diff_count += 1
            return diff_count <= 1

        def find_trans(i, visited, trans):
            word = wordList[i]
            if word == endWord:
                return trans
            min_trans = float('inf')
            for j in range(len(wordList)):
                if not visited[j] and i != j:
                    if has_one_diff(word, wordList[j]):
                        visited[j] = True
                        min_trans = min(min_trans, find_trans(j, visited, trans + 1))
                        visited[j] = False
            return min_trans

        min_trans = float('inf')
        for i, word in enumerate(wordList):
            if word != endWord and has_one_diff(beginWord, word):
                visited = [False for _ in range(len(wordList))]
                visited[i] = True
                min_trans = min(min_trans, find_trans(i, visited, 1))
        return 0 if min_trans==float('inf') else min_trans


sol = Solution()
print(sol.ladderLength("a","c",["a","b","c"]))#2
print(sol.ladderLength(beginWord = "hit",endWord = "cog",wordList = ["hot","dot","dog","lot","log","cog"]))

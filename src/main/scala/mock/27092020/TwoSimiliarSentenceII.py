from collections import defaultdict

class Solution:
    def areSentencesSimilarTwo(self, words1, words2, pairs):
        if len(words1) != len(words2):
            return False
        adj_list = defaultdict(list)

        for word1,word2 in pairs:
            adj_list[word1].append(word2)
            adj_list[word2].append(word1)

        def dfs(adj_list, src, target, seen):
            if src == target:
                return True
            for nei in adj_list[src]:
                if nei == target:
                    return True
                if nei in seen:
                    continue
                seen.add(nei)
                if dfs(adj_list, nei, target, seen):
                    return True
            return False

        for word1,word2 in zip(words1,words2):
            if not dfs(adj_list, word1, word2, set()):
                return False
        return True








class Solution:
    def topologicalSort(self, list,currentVertex, visited, stack):
        visited.add(currentVertex)
        if currentVertex in list.keys():
            for vertex in list[currentVertex]:
                if vertex not in visited:
                    self.topologicalSort(list, vertex, visited, stack)
        stack.insert(0, currentVertex)

    def runTopologicalSort(self, list, words):
        stack = []
        visited = set()
        for n in list.keys():
            if n not in visited:
                self.topologicalSort(list, n, visited, stack)
        return stack


    def has_cycle(self, list):
        if len(list) == 0:
            return False
        for k in list.keys():
            for n in list[k]:
                if n not in list.keys():
                    continue
                for n1 in list[n]:
                    if n1 == k:
                        return True
        return False

    def alienOrder(self, words):
        if not words:
            return ""
        adj_list = {}
        for i in range(len(words) - 1):
            word1 = words[i]
            word2 = words[i+1]
            for j in range(0, min(len(word1), len(word2))):
                if word1[j] != word2[j]:
                    if word1[j] not in adj_list.keys():
                        adj_list[word1[j]] = []
                    adj_list[word1[j]].append(word2[j])
                    break
        if self.has_cycle(adj_list):
            return ""
        res = self.runTopologicalSort(adj_list, words)
        return words[0] if not res and len(words) > 0 else ''.join(res)



sol = Solution()
#print(sol.alienOrder(["zy","zx"])) #yxz
print(sol.alienOrder(["z","z"]))
print(sol.alienOrder(["z","x","z"]))
#print(sol.alienOrder(["aac","aabb","aaba"]))
#"cba"
print(sol.alienOrder([
  "wrt",
  "wrf",
  "er",
  "ett",
  "rftt"
]))
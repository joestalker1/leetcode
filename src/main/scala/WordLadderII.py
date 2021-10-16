from collections import defaultdict


class Solution:
    def findLadders(self, beginWord, endWord, wordList):
        if not wordList or len(wordList[0]) == 0:
            return []
        adj_list = defaultdict(list)
        #generate new adjacent words by changing one char and if they are in word_list
        def find_neighbors(word, word_list):
            nei = []
            chars = list(word)
            for i, ch in enumerate(chars):
                prev = ch
                for c in range(ord('a'), ord('z') + 1):
                    chars[i] = chr(c)
                    new_word = ''.join(chars)
                    if c == prev or new_word not in word_list:
                        continue
                    nei.append(new_word)
                chars[i] = prev
            return nei
        # take for word from adj_lst[src] and try to reach dest
        def backtrack(adj_list, src, dest, cur_path, shortest_path):
            if src == dest:
                shortest_path.append(cur_path[::])
            for w in adj_list[src]:
                cur_path.append(w)
                backtrack(adj_list, w, dest, cur_path, shortest_path)
                cur_path.pop()

        def bfs(adj_list, begin_word, word_list):
            q = [begin_word]
            if begin_word in word_list:
                word_list.discard(begin_word)
            proc = set()
            proc.add(begin_word)
            while q:
                visited = set()
                n = len(q)
                #process only words that deviate by one chars
                for i in range(n):
                    cur_word = q.pop(0)
                    #genereate neighbours for cur_word
                    nei = find_neighbors(cur_word, word_list)

                    for w in nei:
                        #mark as visited
                        visited.add(w)
                        # cur_word -> w
                        adj_list[cur_word].append(w)
                        # if we don't process w, then append it to queue
                        if w not in proc:
                            q.append(w)
                            proc.add(w)
                for w in visited:
                    if w in word_list:
                        word_list.discard(w)

        word_list = set(wordList)
        bfs(adj_list, beginWord, word_list)
        cur_path = [beginWord]
        shortest_path = []
        backtrack(adj_list, beginWord, endWord, cur_path, shortest_path)
        return shortest_path

sol = Solution()
print(sol.findLadders(beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]))
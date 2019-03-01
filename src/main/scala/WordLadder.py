from collections import defaultdict

class Solution:
    def count_diff(self, word1, word2):
        count = 0
        for ch1, ch2 in zip(word1, word2):
            if ch1 != ch2:
                count += 1
            if count > 1:
                return count
        return count

    def ladderLength(self, beginWord: 'str', endWord: 'str', wordList: 'List[str]') -> 'int':
        if not wordList or not beginWord or not endWord:
            return 0
        q = [beginWord]
        seen = set()
        min_len = defaultdict(lambda: 1)
        seen.add(beginWord)
        while len(q) > 0: # N
            word = q.pop(0)
            for word2 in wordList: #N
                if word2 in seen:
                    continue
                if self.count_diff(word, word2) == 1:
                    if word2 == endWord:
                        return min_len[word] + 1
                    min_len[word2] = min_len[word] + 1
                    seen.add(word2)
                    q.append(word2)
        return 0


sol = Solution()
print(sol.ladderLength("hot","dog", ["hot","dog","cog","pot","dot"])) #3
# print(sol.ladderLength("hot", "dog", ["hot", "dog", "dot"]))
# print(sol.ladderLength("qa", "sq",
#                        ["si", "go", "se", "cm", "so", "ph", "mt", "db", "mb", "sb", "kr", "ln", "tm", "le", "av", "sm",
#                         "ar", "ci", "ca", "br", "ti", "ba", "to", "ra", "fa", "yo", "ow", "sn", "ya", "cr", "po", "fe",
#                         "ho", "ma", "re", "or", "rn", "au", "ur", "rh", "sr", "tc", "lt", "lo", "as", "fr", "nb", "yb",
#                         "if", "pb", "ge", "th", "pm", "rb", "sh", "co", "ga", "li", "ha", "hz", "no", "bi", "di", "hi",
#                         "qa", "pi", "os", "uh", "wm", "an", "me", "mo", "na", "la", "st", "er", "sc", "ne", "mn", "mi",
#                         "am", "ex", "pt", "io", "be", "fm", "ta", "tb", "ni", "mr", "pa", "he", "lr", "sq", "ye"]))
#
# print(sol.ladderLength("hot", "dog", ["hot", "cog", "dog", "tot", "hog", "hop", "pot", "dot"]))  # 3
# print(sol.ladderLength("a", "c", ["a", "b", "c"]))
print(sol.ladderLength("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))

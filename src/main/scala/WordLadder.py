from collections import defaultdict

class Solution:
    def can_trans(self, word1, word2):
        diff_count = 0
        for i in range(len(word1)):
            if word1[i] != word2[i]:
                diff_count += 1
            if diff_count > 1:
                return False
        return diff_count <= 1

    def generate_words(self, word):
        for i in range(len(word)):
            yield word[0:i] + '*'+word[i + 1:]


    def ladderLength(self, beginWord: 'str', endWord: 'str', wordList: 'List[str]') -> 'int':
        if not wordList or not beginWord or not endWord:
            return 0
        all_dict = defaultdict(list)
        for temp in self.generate_words(beginWord):
            all_dict[temp].append(beginWord)

        for word in wordList:
            for temp in self.generate_words(word):
                all_dict[temp].append(word)

        q = [[beginWord, 1]]
        seen = set()
        seen.add(beginWord)
        while q:
            word, d = q.pop(0)
            for temp in self.generate_words(word):
                for candidate in all_dict[temp]:
                    if candidate == endWord:
                        return d + 1
                    if candidate is seen:
                        continue
                    seen.add(candidate)
                    q.append([candidate,d+1])
                all_dict[temp] = []   # important optimization !!!
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
print(sol.ladderLength("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))#5

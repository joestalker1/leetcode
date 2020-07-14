from collections import defaultdict


class Solution:
    def generate_patterns(self, word):
        for i in range(len(word)):
            yield word[0:i] + '*' + word[i + 1:]

    def ladderLength(self, beginWord: 'str', endWord: 'str', wordList: 'List[str]') -> 'int':
        if not wordList or not beginWord or not endWord:
            return 0
        all_dict = defaultdict(list)
        for pat in self.generate_patterns(beginWord):
            all_dict[pat].append(beginWord)

        for word in wordList:
            for pat in self.generate_patterns(word):
                all_dict[pat].append(word)

        q = [[beginWord, 1]]
        seen = set()
        seen.add(beginWord)
        while q:
            word, d = q.pop(0)
            for pat in self.generate_patterns(word):
                for candidate in all_dict[pat]:
                    if candidate == endWord:
                        return d + 1
                    if candidate is seen:
                        continue
                    seen.add(candidate)
                    q.append([candidate, d + 1])
                all_dict[pat] = []  # important optimization !!!
        return 0


sol = Solution()
print(sol.ladderLength("hot", "dog", ["hot", "dog", "cog", "pot", "dot"]))  # 3
# print(sol.ladderLength("hot", "dog", ["hot", "dog", "dot"]))
print(sol.ladderLength("qa", "sq",
                       ["si", "go", "se", "cm", "so", "ph", "mt", "db", "mb", "sb", "kr", "ln", "tm", "le", "av", "sm",
                        "ar", "ci", "ca", "br", "ti", "ba", "to", "ra", "fa", "yo", "ow", "sn", "ya", "cr", "po", "fe",
                        "ho", "ma", "re", "or", "rn", "au", "ur", "rh", "sr", "tc", "lt", "lo", "as", "fr", "nb", "yb",
                        "if", "pb", "ge", "th", "pm", "rb", "sh", "co", "ga", "li", "ha", "hz", "no", "bi", "di", "hi",
                        "qa", "pi", "os", "uh", "wm", "an", "me", "mo", "na", "la", "st", "er", "sc", "ne", "mn", "mi",
                        "am", "ex", "pt", "io", "be", "fm", "ta", "tb", "ni", "mr", "pa", "he", "lr", "sq", "ye"]))
#
# print(sol.ladderLength("hot", "dog", ["hot", "cog", "dog", "tot", "hog", "hop", "pot", "dot"]))  # 3
# print(sol.ladderLength("a", "c", ["a", "b", "c"]))
print(sol.ladderLength("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))  # 5

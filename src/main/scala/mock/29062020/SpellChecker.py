from collections import defaultdict


class Solution:
    def spellchecker(self, wordlist, queries):
        if not wordlist and not queries:
            return []

        def match(m, word):
            if word in m:
                return m[word][0]
            return -1

        def replace_by_star(word, vowels):
            res = []
            for ch in word:
                if ch in vowels:
                    res.append('*')
                else:
                    res.append(ch)
            return ''.join(res)

        vowels = set(['a', 'e', 'i', 'o', 'u'])
        words = defaultdict(list)
        captWordList = defaultdict(list)
        vowelWordList = defaultdict(list)
        for i, word in enumerate(wordlist):
            words[word].append(i)
            to_lower = word.lower()
            captWordList[to_lower].append(i)
            repl = replace_by_star(word.lower(), vowels)
            vowelWordList[repl].append(i)

        res = []
        for query in queries:
            to_lower = query.lower()
            i1 = match(words, query)
            if i1 >= 0:
                res.append(wordlist[i1])
                continue
            i2 = match(captWordList, to_lower)
            if i2 >= 0:
                res.append(wordlist[i2])
                continue
            i3 = match(vowelWordList, replace_by_star(to_lower, vowels))
            if i3 >= 0:
                res.append(wordlist[i3])
            else:
                res.append("")
        return res


sol = Solution()
print(sol.spellchecker(["KiTe", "kite", "hare", "Hare"],
                       ["kite", "Kite", "KiTe", "Hare", "HARE", "Hear", "hear", "keti", "keet", "keto"]))
# ["kite","KiTe","KiTe","Hare","hare","","","KiTe","","KiTe"]

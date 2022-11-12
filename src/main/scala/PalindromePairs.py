class Solution:
    def palindromePairs(self, words):
        # assert self._palindromePairs(['abcd','dcba','lls','s','sssll']) == [[0,1],[1,0],[3,2],[2,4]],'test1'
        # assert self._palindromePairs(['bat','tab','cat']) == [[0,1],[1,0]], 'test2'
        # assert self._palindromePairs([]) == [],'test3'
        # asset self._palindromePairs(['a','b','c','ab','ac','aa']) == [[3,0],[1,3],[4,0],[2,4],[5,0],[0,5]],'test4'
        return self._palindromePairs(words)

    def palindromePairs(self, words):

        def all_valid_prefixes(word):
            valid_prefixes = []
            for i in range(len(word)):
                if word[i:] == word[i:][::-1]:
                    valid_prefixes.append(word[:i])
            return valid_prefixes

        def all_valid_suffixes(word):
            valid_suffixes = []
            for i in range(len(word)):
                if word[:i + 1] == word[:i + 1][::-1]:
                    valid_suffixes.append(word[i + 1:])
            return valid_suffixes

        word_lookup = {word: i for i, word in enumerate(words)}
        solutions = []

        for i, word in enumerate(words):
            reversed_word = word[::-1]
            if reversed_word in word_lookup and i != word_lookup[reversed_word]:
                solutions.append([i, word_lookup[reversed_word]])

            for suffix in all_valid_suffixes(word):
                reversed_suffix = suffix[::-1]
                if reversed_suffix in word_lookup:
                    solutions.append([word_lookup[reversed_suffix], i])

            for prefix in all_valid_prefixes(word):
                reversed_prefix = prefix[::-1]
                if reversed_prefix in word_lookup:
                    solutions.append([i, word_lookup[reversed_prefix]])

        return solutions
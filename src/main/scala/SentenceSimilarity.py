class Solution:
    def areSentencesSimilar(self, words1, words2, pairs):
        if not words2 and not words1:
            return True
        if not words1 or not words2 or len(words1) != len(words2):
            return False
        encoding = set()
        for w1,w2 in pairs:
            encoding.add((w1,w2))

        for i in range(len(words1)):
            if words1[i] != words2[i] and (words1[i], words2[i]) not in encoding and (words2[i], words1[i]) not in encoding:
                return False
        return True



sol = Solution()
print(sol.areSentencesSimilar(["an", "extraordinary", "meal"], ["one", "good", "dinner"],
                              [["great", "good"], ["extraordinary", "good"], ["well", "good"], ["wonderful", "good"],
                               ["excellent", "good"], ["fine", "good"], ["nice", "good"], ["any", "one"],
                               ["some", "one"], ["unique", "one"], ["the", "one"], ["an", "one"], ["single", "one"],
                               ["a", "one"], ["truck", "car"], ["wagon", "car"], ["automobile", "car"], ["auto", "car"],
                               ["vehicle", "car"], ["entertain", "have"], ["drink", "have"], ["eat", "have"],
                               ["take", "have"], ["fruits", "meal"], ["brunch", "meal"], ["breakfast", "meal"],
                               ["food", "meal"], ["dinner", "meal"], ["super", "meal"], ["lunch", "meal"],
                               ["possess", "own"], ["keep", "own"], ["have", "own"], ["extremely", "very"],
                               ["actually", "very"], ["really", "very"], ["super", "very"]]))
print(sol.areSentencesSimilar(["w1"], ["w1"], []))
print(sol.areSentencesSimilar(["great", "acting", "skills"], ["fine", "painting", "talent"],
                              [["great", "fine"], ["drama", "acting"], ["skills", "talent"]]))

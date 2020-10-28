class Solution:
    def areSentencesSimilar(self, sentence1, sentence2, similarPairs):
        if len(sentence1) != len(sentence2):
            return False
        sim = {}
        for word1,word2 in similarPairs:
            sim[word1] = word2

        for i in range(len(sentence1)):
            word1 = sentence1
            word2 = sentence2
            if word1 == word2 or sim[word1] == word2 or sim[word2] == word1:
                continue
            else:
                return False
        return True

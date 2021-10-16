from collections import Counter

class Solution:
    def checkIfPangram(self, sentence):
        count = Counter(sentence)
        return len(count) == 28
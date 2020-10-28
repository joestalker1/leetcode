class Solution:
    def findOcurrences(self, text: str, first: str, second: str):
        if not text or not first or not second:
            return []

        words = text.split(" ")
        res = []
        for i in range(len(words)):
            if i + 2 < len(words) and words[i] == first and words[i+1] == second:
                res.append(words[i+2])
        return res



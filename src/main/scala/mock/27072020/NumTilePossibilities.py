from collections import Counter

class Solution:
    def numTilePossibilities(self, tiles):
        if not tiles or len(tiles) == 0:
            return 0
        words = {c for c in tiles}

        for l in range(2, len(tiles)+1):
            new_words = []
            for word in words:
                if len(word) == l-1:
                    freq = Counter(tiles)
                    for ch in word:
                        freq[ch] -= 1
                    for ch in tiles:
                        if freq[ch] > 0:
                            new_words.append(word+ch)
            for word in new_words:
                words.add(word)
        return len([1 for t in words if len(t) > 0])


sol = Solution()
#"A", "B", "AA", "AB", "BA", "AAB", "ABA", "BAA"
print(sol.numTilePossibilities("AAB"))

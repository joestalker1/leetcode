class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        if not keyboard or not word:
            return 0
        key_to_index = {}
        for i, ch in enumerate(keyboard):
            key_to_index[ch] = i
        last = 0
        t = 0
        for ch in word:
            t += abs(key_to_index[ch] - last)
            last = key_to_index[ch]
        return t

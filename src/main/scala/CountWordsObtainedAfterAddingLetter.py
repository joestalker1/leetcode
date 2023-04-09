from collections import defaultdict

class Solution:
    def wordCount(self, startWords, targetWords) -> int:

        def conv_to_mask(word):
            mask = 0
            for ch in word:
                mask |= 1 << (ord(ch) - ord('a'))
            return mask

        converted = 0
        start_word_masks = set()
        for word in startWords:
            start_word_masks.add(conv_to_mask(word))

        for word in targetWords:
            to_mask = conv_to_mask(word)
            for ch in word:
                from_mask = to_mask ^ (1 << (ord(ch) - ord('a')))
                if from_mask in start_word_masks:
                    converted += 1
                    break
        return converted
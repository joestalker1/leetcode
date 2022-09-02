class Solution:
    def uniqueLetterString(self, s: str) -> int:
        if not s:
            return 0
        # last pos where we encounter char last time.
        last_pos = [0] * 27
        # number of substr ending with char
        contrib = [0] * 27
        uniq_char = 0
        # current values of unique chars in substring from till i
        cur = 0
        for i, ch in enumerate(s):
            code = ord(ch) - ord('A')
            # subtract previous contribution ch from current sum of all substring
            cur -= contrib[code]
            # if there is else such char then don't count num of uniq chars ending at last_pos
            contrib[code] = i - (last_pos[code] - 1)
            # count new sum of uniq substring
            cur += contrib[code]
            uniq_char += cur
            last_pos[code] = i + 1
        return uniq_char
    

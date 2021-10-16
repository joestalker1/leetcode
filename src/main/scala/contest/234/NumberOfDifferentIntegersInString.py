class Solution:
    def numDifferentIntegers(self, word: str):
        if not word:
            return 0
        nums = set()
        buf = []
        for ch in word:
            if '0' <= ch <= '9':
                buf.append(ch)
            else:
                if buf:
                    nums.add(int(''.join(buf)))
                buf = []
        if buf:
            nums.add(int(''.join(buf)))
        return len(nums)


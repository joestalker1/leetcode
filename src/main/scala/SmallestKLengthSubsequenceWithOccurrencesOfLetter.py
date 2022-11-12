class Solution:
    def smallestSubsequence(self, s: str, k: int, letter: str, repetition: int) -> str:
        if not s:
            return ''
        st = []
        #number of letter is left
        total_letter = len([c for c in s if c == letter])
        #repetition is number of letter is needed to place in stack
        for i,ch in enumerate(s):
            while st and st[-1] > ch and (len(s) - i + len(st)) > k and (st[-1] != letter or total_letter > repetition):
                c = st.pop()
                if c == letter:
                    repetition += 1
            if len(st) < k:
                if ch == letter:
                    st.append(ch)
                    repetition -= 1
                elif k - len(st) > repetition:
                    st.append(ch)
            if ch == letter:
                total_letter -= 1
        return ''.join(st)
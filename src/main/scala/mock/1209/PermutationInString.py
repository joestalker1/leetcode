class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # assert self._checkInclusion('a','aaa') == True, 'test1'
        # assert self._checkInclusion('ba','abc') == True, 'test2'
        # assert self._checkInclusion('aba','abc') == False, 'test3'
        return self._checkInclusion(s1,s2)

    def _checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        freq_s1 = [0] * 26
        freq_s2 = [0] * 26

        def code(ch):
            return ord(ch) - ord('a')

        for i in range(len(s1)):
            freq_s1[code(s1[i])] += 1
            freq_s2[code(s2[i])] += 1
        cnt = 0
        for i in range(26):
            if freq_s1[i] == freq_s2[i]:
                cnt += 1
        for i in range(len(s2) - len(s1)):
            if cnt == 26:
                return True
            ch1 = code(s2[i])
            ch2 = code(s2[i+len(s1)])
            freq_s2[ch2] += 1
            if freq_s1[ch2] == freq_s2[ch2]:
                cnt += 1
            if freq_s2[ch2] == freq_s1[ch2] + 1:
                cnt -= 1
            freq_s2[ch1] -= 1
            if freq_s1[ch1] == freq_s2[ch1]:
                cnt += 1
            elif freq_s1[ch1] == freq_s2[ch1] + 1:
                cnt -= 1
        return cnt == 26

sol = Solution()
print(sol.checkInclusion("adc", "dcda"))#true
print(sol.checkInclusion(s1 = "ab", s2 = "baooo"))


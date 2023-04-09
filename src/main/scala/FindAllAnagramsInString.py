class Solution:

    def findAnagrams(self, s: str, p: str) -> List[int]:
        if s == p:
            return [0]
        if not s or not p:
            return []
        freq_p = [0] * 26

        def code(ch):
            return ord(ch) - ord('a')

        for ch in p:
            freq_p[code(ch)] += 1
        anag_index = []
        cur_freq = [0] * 26
        for i, ch in enumerate(s):
            cur_freq[code(ch)] += 1
            if i >= len(p):
                cur_freq[code(s[i - len(p)])] -= 1
            matched = True
            for j in range(26):
                if cur_freq[j] != freq_p[j]:
                    matched = False
                    break
            if matched:
                anag_index.append(i - len(p) + 1)
        return anag_index


sol = Solution()
print(sol.findAnagrams("abaacbabc", "abc"))  # [3,4,6]
# print(sol.findAnagrams("abacbabc", "abc"))
print(sol.findAnagrams("abab", "ab"))
print(sol.findAnagrams("cbaebabacd", "abc"))

class Solution:
    def minDeletions(self, s: str) -> int:
        if len(s) < 2:
            return 0
        freq = [0] * 26
        for ch in s:
            freq[ord(ch)-ord('a')] += 1
        max_freq_allowed = len(s)
        freq.sort(reverse=True)
        need_delete = 0
        for i in range(len(freq)):
            if freq[i] > max_freq_allowed:
                need_delete += freq[i] - max_freq_allowed
                freq[i] = max_freq_allowed
            max_freq_allowed = max(0, freq[i] - 1)
        return need_delete
from collections import defaultdict,Counter
class Solution:
    def wordCount(self, startWords, targetWords) -> int:
        cnt = 0
        len_to_word = defaultdict(list)
        for i,word in enumerate(startWords):
            len_to_word[len(word)].append(i)
        for word in targetWords:
            need_len = len(word) - 1
            if not len_to_word[need_len]:
                continue
            freq1 = Counter(word)
            for i in len_to_word[need_len]:
                freq2 = Counter(startWords[i])
                bad = False
                for ch in freq2:
                    if ch not in freq2 or freq2[ch] == 0:
                        bad = True
                        break
                    freq2[ch] -= 1
                    freq1[ch] -= 1
                if bad:
                    continue
                bad = False
                for ch in freq2:
                    if freq2[ch] > 0:
                        bad = True
                        break
                left = 0
                for ch in freq1:
                    if freq1[ch] > 0:
                        left += 1
                if left == 1 and not bad:
                    cnt += 1
        return cnt


sol = Solution()
print(sol.wordCount(["ant","act","tack"], ["tack","act","acti"]))#2
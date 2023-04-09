class Solution:
    def uniqueLetterString(self, s: str) -> int:
        def code(ch):
            return ord(ch) - ord('A')

        last_pos = [0] * 26
        substr_cnt = [0] * 26
        cur_cnt = 0
        total = 0
        for i in range(len(s)):
            #get code of s[i]
            c = code(s[i])
            #substract previous number of substring contain s[i]
            cur_cnt -= substr_cnt[c]
            #number of substrings ends at i and have one s[i]
            substr_cnt[c] = i - last_pos[c] + 1
            #update new substring with one s[i]
            cur_cnt += substr_cnt[c]
            total += cur_cnt
            last_pos[c] = i + 1
        return total
    

class Solution:
    def findAnagrams(self, s, p):
        def equals(dict1, dict2):
            for ch,count in dict1.items():
                if ch not in dict2:
                    return False
                else:
                    c1 = dict2[ch]
                    if c1 != count:
                        return False
            return True

        if len(p) == 0 or len(s) == 0:
            return []
        dict1 = {}
        for ch in p:
            if ch in dict1:
                dict1[ch] = dict1[ch] + 1
            else:
                dict1[ch] = 1

        i = 0
        word = {}
        len1 = len(p)
        indices = []
        while (i + len1) <= len(s):
            if i == 0:
               for j in range(len1):
                   if s[j] in word:
                       word[s[j]] = word[s[j]] + 1
                   else:
                       word[s[j]] = 1
            else:
                # remove i-1 character from word
                ch1 = s[i-1]
                c = word[ch1]
                if c - 1 >= 0:
                    word[ch1] = c - 1
                else:
                    del word[ch1]
                # add i + len1 character to word
                ch1 = s[i + len1 - 1]
                if ch1 in word:
                    word[ch1] = word[ch1] + 1
                else:
                    word[ch1] = 1

            if equals(dict1, word):
                indices.append(i)
            i = i + 1
        return indices


sol = Solution()
print(sol.findAnagrams("cbaebabacd", "abc"))
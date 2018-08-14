class Solution:
    def findAnagrams(self, s, p):
        if len(p) == 0 or len(s) == 0:
            return []
        dict1 = {}
        for ch in p:
            if ch in dict1:
                dict1[ch] = dict1[ch] + 1
            else:
                dict1[ch] = 1

        i = 0
        indices = []
        while i < len(s):
            j = i
            anag = {}
            len1 = 0
            while j < len(s):
                ch = s[j]
                if ch in dict1:
                    if ch in anag:
                        c1 = anag[ch]
                        c2 = dict1[ch]
                        if c1 + 1 <= c2:
                            anag[ch] = c1 + 1
                            len1 += 1
                        else:
                            j = len(s)
                    else:
                        anag[ch] = 1
                        len1 += 1
                if len(p) == len1:
                    indices.append(i)
                    j = len(s)
                j = j + 1
            i = i + 1
        return indices


sol = Solution()
print(sol.findAnagrams("baa", "aa"))
class Solution:
    def firstUniqChar(self, s):
        dict1 = {}
        indices = []
        for i in range(len(s)):
            ch = s[i]
            if ch in dict1:
                c = dict1[ch]
                dict1[ch] = c + 1
            else:
                dict1[ch] = 1
                indices.append(i)
        for i in range(len(indices)):
            j = indices[i]
            c = dict1[s[j]]
            if c == 1:
                return j

s = "loveleetcod"
sol = Solution()
print(sol.firstUniqChar(s))
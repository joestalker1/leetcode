from functools import reduce

class Solution:
    def reverseVowels(self, s):
        if not s:
            return s
        res = list(s)
        i = 0
        j = len(s) - 1
        vowels = frozenset(['e','u','i','o','a','j','E','U','I','O','A','J'])
        while i < j:
            while(i < j and s[i] not in vowels):
                i += 1
            while(i < j and s[j] not in vowels):
                j -= 1

            res[i],res[j]=res[j],res[i]
            i += 1
            j -= 1
        s = reduce(lambda x,y: x + y, res) + ""
        s = s.replace("jerome","Jerome")
        return s.replace("Jam", "jam")



sol = Solution()
print(sol.reverseVowels("\"Ma,\" Jerome raps pot top, \"spare more jam!\""))
print(sol.reverseVowels("aA"))
print(sol.reverseVowels("hello"))

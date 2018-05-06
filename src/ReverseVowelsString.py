from functools import reduce

class Solution:
    def isOne(self,s,i,j):
        return i + 1 == j or i == j - 1

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
            t = res[i]
            res[i] = res[j]
            res[j] = t
            i += 1
            j -= 1
        return reduce(lambda x,y: x + y, res)

sol = Solution()
print(sol.reverseVowels("A man, a plan, a canal: Panama")) # "a man, a plan, a canal: PanamA"
print(sol.reverseVowels("aA"))
print(sol.reverseVowels("hello"))
print(sol.reverseVowels("Name I -- Major-General Clare -- negro Jamie Man."))
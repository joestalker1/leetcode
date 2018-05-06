class Solution:
    def findLUSlength(self, a, b):
        if a == b:
            return -1
        if len(a) < len(b):
            s1,s2 = a,b
        else:
            s1,s2 = b,a
        result = 0
        l = 0
        while l < len(s1):
            i = 0
            while i < len(s2):
                j = l
                k = i
                while j < len(s1) and k < len(s2) and s1[j] != s2[k]:
                    k += 1
                    j += 1
                if k == len(s2) and j < len(s1):
                    result = max(result, len(s1) - j + len(s2) - i)
                elif j == len(s1) and k < len(s2):
                    result = max(result, len(s2) - k + len(s1) - l)
                else:
                    result = max(result, j - l)
                i += 1
            l += 1
        if not result:
            result = -1
        return result


sol = Solution()
print(sol.findLUSlength("aweffwaf", "aweffwaf"))
print(sol.findLUSlength("abc","bda"))
print(sol.findLUSlength("aefawfawfawfaw", "aefawfeawfwafwaef"))
class Solution:
    def canConvert(self, str1: str, str2: str) -> bool:
        if not str1 and not str2 or str1 == str2:
            return True
        if len(str1) != len(str2):
            return False
        # if str2 has 26 char we can't use free chars in intermidiate transformation
        if len(set(str2)) == 26:
            return False
        m = {}
        for ch1,ch2 in zip(str1,str2):
            if ch1 not in m:
                m[ch1] = ch2
            elif m[ch1] != ch2:
                return False
        return True


sol = Solution()
print(sol.canConvert("abcdefghijklmnopqrstuvwxyz", "bcdefghijklmnopqrstuvwxyza"))#false
print(sol.canConvert("abcdefghijklmnopqrstuvwxy", "bcdefghijkamnopqrstuvwxyz"))#true

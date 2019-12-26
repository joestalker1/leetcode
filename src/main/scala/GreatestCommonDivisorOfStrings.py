class Solution:
    def has_gcd(self, str1, gcd):
        if len(str1) < len(gcd) or len(str1) % len(gcd) != 0:
            return False
        i = 0
        while i < len(str1):
            for j in range(len(gcd)):
                if str1[i + j] != gcd[j]:
                    return False
            i += len(gcd)
        return True

    def gcdOfStrings(self, str1, str2):
        if not str1 or not str2:
            return ""
        if len(str1) < len(str2):
            t = str1
            str1 = str2
            str2 = t
        for i in range((len(str1) // 2 + 1), 0, -1):
            gcd = str1[0: i]
            if self.has_gcd(str1, gcd) and self.has_gcd(str2, gcd):
                return gcd
        return ""

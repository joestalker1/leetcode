class Solution:
    def gcd(self, str1):
        len_s =len(str)
        while len_s % 2 == 0:
            part_len = len_s // 2
            if str1[0:]
        m = {}
        gcd1 = []
        for ch in str1:
            if ch not in m:
                if meet == 1:
                    gcd1.append(ch)
                    m[ch] = meet
                else:
                    return False
            else:
                meet += 1
                m[ch] = meet
        return ''.join(gcd1)

    def gcdOfStrings(self, str1, str2):
        if not str1 or not str2:
            return False
        gcd1 = self.gcd(str1)
        gcd2 = self.gcd(str2)
        if gcd1 and gcd1 == gcd2:
            return gcd1
        return ""

sol = Solution()
print(sol.gcdOfStrings("TAUXXTAUXXTAUXXTAUXXTAUXX", "TAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXX"))







class Solution:
    def isIsomorphic(self, s: str, t: str):
        if not s and not t:
            return True
        if len(s) != len(t):
            return False

        m = {}
        # store chars from t if they are mapped to other chars from s
        used = set()
        for i in range(len(s)):
            ch1 = s[i]
            ch2 = t[i]
             # if ch1 is in m and not to map to ch2 or has been used earlier,return False
            if ch1 in m and m[ch1] != ch2 or ch1 not in m and ch2 in used:
                return False
            m[ch1] = ch2
            used.add(ch2)
        return True



class Solution:
    def areAlmostEqual(self, s1: str, s2: str):
        if s1 == s2:
            return True
        if not s1 or not s2 or len(s1) != len(s2) or set(s1) != set(s2):
            return False
        cnt = 0
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                cnt += 1
        return cnt == 2

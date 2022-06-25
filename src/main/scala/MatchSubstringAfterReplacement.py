from collections import defaultdict

class Solution:
    def matchReplacement(self, s: str, sub: str, mappings) -> bool:
        if not s or not sub:
            return False
        sub_to_s = defaultdict(dict)
        for old, new in mappings:
            sub_to_s[old][new] = 1

        def check(s, sub, i, sub_to_s):
            if i + len(sub) > len(s):
                return False
            j = 0
            for k in range(i, i + len(sub)):
                if s[k] == sub[j] or s[k] in sub_to_s[sub[j]]:
                    j += 1
                else:
                    return False
            return True

        for i in range(len(s)):
            if check(s, sub, i, sub_to_s):
                return True
        return Fals
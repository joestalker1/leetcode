class Solution:
    def canConvert(self, str1: str, str2: str) -> bool:
        if not str1 and not str2 or str1 == str2:
            return True
        if len(str1) != len(str2):
            return False
        mapping = {}
        for i in range(len(str1)):
            ch = str1[i]
            if ch not in mapping:
                mapping[ch] = str2[i]
            else:
                if mapping[ch] != str2[i]:
                    return False
        return True

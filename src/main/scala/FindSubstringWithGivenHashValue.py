class Solution:
    def subStrHash(self, s: str, power: int, modulo: int, k: int, hashValue: int) -> str:
        if not s:
            return ''
        cur_hash = 0
        pk = 1
        j = 0
        for i in range(len(s)-1,-1,-1):
            cur_hash = (cur_hash * power + ord(s[i]) - ord('a') + 1 ) % modulo
            if i + k >= len(s):
                pk = pk * power % modulo
            else:
                cur_hash = (cur_hash - (ord(s[i+k]) - ord('a') + 1) * pk % modulo + modulo) % modulo
            if cur_hash == hashValue:
                j = i
        return s[j:j + k]

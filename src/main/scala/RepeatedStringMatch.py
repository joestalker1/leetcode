class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        if a == b:
            return 1

        def rabin_karp(txt, pat):
            if not txt or not pat:
                return False
            p = 1
            base = 10 ** 9 + 7
            m = len(pat)
            for i in range(m):
                p = (p * 31) % base
            pat_code = 0
            for i in range(m):
                pat_code = (pat_code * 31 + ord(pat[i])) % base
            hash_code = 0
            for i in range(len(txt)):
                hash_code = (31 * hash_code + ord(txt[i])) % base
                if i < m - 1:
                    continue
                if i >= m:
                    hash_code = (hash_code - ord(txt[i - m]) * p) % base
                if hash_code < 0:
                    hash_code += base
                if hash_code == pat_code and txt[i - m + 1:i + 1] == pat:
                    return True
            return False

        cnt = 1
        aa = a
        while len(aa) < len(b):
            cnt += 1
            aa += a
        if aa == b:
            return cnt
        if rabin_karp(aa, b):
            return cnt
        if rabin_karp(aa + a, b):
            return cnt + 1
        return -1



sol = Solution()
print(sol.repeatedStringMatch("aabaa", "aaab")) # 2
print(sol.repeatedStringMatch( "abcd", "cdabcdab"))
print(sol.repeatedStringMatch("abcd", "abcdb"))

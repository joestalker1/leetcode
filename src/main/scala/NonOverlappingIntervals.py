import math


class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        poly = []
        for i in range(2 * len(s)):
            l = i // 2
            r = l + i % 2
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r - l + 1 >= k:
                    poly.append([l,r+1])
                    break
                l-= 1
                r += 1
        poly.sort(key=lambda x:x[1])
        cnt = 0
        last = -math.inf
        for l,r in poly:
            if l >= last:
                cnt += 1
                last = r
            else:
                if r < last:
                    last = r
        return cnt



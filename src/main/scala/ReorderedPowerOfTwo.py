from collections import Counter

class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        if n & (n-1) == 0:
            return True
        digits = Counter(str(n))
        return any(digits == Counter(str(1 << b)) for b in range(31))



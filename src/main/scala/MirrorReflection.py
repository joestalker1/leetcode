class Solution:
    def mirrorReflection(self, p: int, q: int) -> int:

        def gcd(a, b):
            if b == 0:
                return a
            return gcd(b, a % b)

        g = gcd(p, q)
        max_wall = (q * p) // g
        ref_num = max_wall // q
        room_num = max_wall // p
        if ref_num % 2 == 0:
            # ray is on the left-side,let return 2
            return 2
        if room_num % 2 == 0:
            return 0
        return 1
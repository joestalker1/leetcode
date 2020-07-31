class Solution:
    def largestTimeFromDigits(self, A):
        digits = A
        ans = -1
        for cur in range(24 * 60):
            h = cur // 60
            m = cur % 60
            h1 = h // 10
            h2 = h % 10
            m1 = m // 10
            m2 = m % 10
            if h1 not in digits or h2 not in digits or m2 not in digits or m1 not in digits:
                continue
            used = set()
            for a in digits:
                if a == h1 and 0 not in used:
                    used.add(0)
                elif a == h2 and 1 not in used:
                    used.add(1)
                elif a == m1 and 2 not in used:
                    used.add(2)
                elif a == m2 and 3 not in used:
                    used.add(3)

            if len(used) == 4:
                ans = cur
        return "{:02d}:{:02d}".format(ans // 60, ans % 60) if ans > -1 else ""


sol = Solution()
print(sol.largestTimeFromDigits([1,2,3,4]))
print(sol.largestTimeFromDigits([0,0,1,0]))
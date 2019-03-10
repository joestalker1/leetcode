import random

class Solution:
    def __init__(self, w):
        self.psum = []
        self.total = 0
        for i in range(len(w)):
            self.total += w[i]
            self.psum.append(self.total)

    def pickIndex(self):
        a = random.randint(0, self.total - 1)
        lo = 0
        hi = len(self.psum) - 1
        while lo != hi:
            mid = lo + (hi - lo) // 2
            if a >= self.psum[mid]:
                lo = mid + 1
            else:
                hi = mid
        return lo



sol = Solution([1])
print(sol.pickIndex())
print(sol.pickIndex())
print(sol.pickIndex())
print(sol.pickIndex())
print(sol.pickIndex())
# sol = Solution([0,3])
# print(sol.pickIndex())
# print(sol.pickIndex())
# print(sol.pickIndex())
# print(sol.pickIndex())
# print(sol.pickIndex())







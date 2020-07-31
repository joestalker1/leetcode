class NumArray:

    def __init__(self, nums):
        self.n = len(nums)
        self.tree = [0] * (2 *self.n)
        i = self.n
        j = 0
        while i < 2*self.n:
            self.tree[i] = nums[j]
            i += 1
            j += 1
        i = self.n-1
        while i>= 0:
            self.tree[i] = self.tree[2*i]+self.tree[2*i + 1]
            i -= 1


    def update(self, pos: int, val: int) -> None:
        pos += self.n
        self.tree[pos] = val
        while pos > 0:
            left = pos
            right = pos
            if pos % 2 == 0:
                right = pos + 1
            else:
                left = pos - 1
            self.tree[pos//2] = self.tree[left] + self.tree[right]
            pos = pos // 2

    def sumRange(self, l, r):
        l += self.n
        r += self.n
        sum = 0
        while l <= r:
            if r % 2 == 0:
                sum += self.tree[r]
                r -= 1
            if l % 2 == 1:
                sum += self.tree[l]
                l += 1
            l = l // 2
            r = r // 2
        return sum
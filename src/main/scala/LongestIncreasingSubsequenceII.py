class SegmentTree:
    def __init__(self, n):
        self.tree = [0] * (2 * n)
        self.sz = n

    def query(self, l, r):
        l += self.sz
        r += self.sz
        max_val = 0
        while l < r:
            if l & 1:
                max_val = max(max_val, self.tree[l])
                l += 1
            if r & 1:
                r -= 1
                max_val = max(max_val, self.tree[r])
            l >>= 1
            r >>= 1
        return max_val

    def update(self, i, val):
        i += self.sz
        self.tree[i] = val
        while i > 1:
            i >>= 1
            self.tree[i] = max(self.tree[2 * i], self.tree[2 * i + 1])


class Solution:
    def lengthOfLIS(self, nums, k: int) -> int:
        # assert self._lengthOfLIS([3,1,3,4,5],1) == 3, 'test1'
        # assert self._lengthOfLIS([1],1) == 1, 'test2'
        # assert self._lengthOfLIS([5,4,3,2,1],1) == 1, 'test3'
        # assert self._lengthOfLIS([1,3,5,7,9],1) == 1, 'test4'
        return self._lengthOfLIS(nums, k)

    def _lengthOfLIS(self, nums, k: int) -> int:
        if not nums or k == 0:
            return 0
        max_val = max(nums)
        seg_tree = SegmentTree(max_val + 1)
        max_sub_len = 1
        for num in nums:
            cur_len = seg_tree.query(max(0, num - k), num)
            max_sub_len = max(max_sub_len, cur_len + 1)
            seg_tree.update(num, cur_len + 1)
        return max_sub_len
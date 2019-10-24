import math

class SegmentTree:
    def __init__(self, n):
        sz = 2 * (2 ** (math.log(n) + 1))
        self.seg_tree = [0] * int(sz)

    def build(self, code, arr, node, b, e):
        if b == e:
            if code == 0:#range_sum
                self.seg_tree[node] = arr[b]
            else:
                self.seg_tree[node] = b
        else:
            left_idx = 2 * node
            right_idx = 2 * node + 1
            self.build(code, arr, left_idx, b, (b + e) // 2)
            self.build(code, arr, right_idx, (b + e) // 2 + 1, e)
            l_content = self.seg_tree[left_idx]
            r_content = self.seg_tree[right_idx]
            if code == 0:
                self.seg_tree[node] = l_content + r_content
            else:
                l_val = arr[l_content]
                r_val = arr[r_content]
                if code == 1:#range_min
                    self.seg_tree[node] = l_content if l_val <= r_val else r_content
                else:
                    self.seg_tree[node] = l_content if l_val >= r_val else r_content

    def query(self, code, arr, node, b, e, i, j):
        if i > e or j < b:
            return -1 #; // if the current interval does not intersect query interval
        if b >= i and e <= j:
            return self.seg_tree[node]

        p1 = self.query(code, arr, 2 * node, b, (b + e) // 2, i, j)
        p2 = self.query(code, arr, 2 * node + 1, (b + e) // 2 + 1, e, i, j)
        if p1 == -1:
            return p2
        if p2 == -1:
            return p1

        if code == 0:
            return p1 + p2
        if code == 1:
            return p1 if arr[p1] <= arr[p2] else p2
        return p1 if arr[p1] >= arr[p2] else p2


arr = [8, 7, 3, 9, 5, 1, 10]
seg_tree = SegmentTree(len(arr))
seg_tree.build(1, arr, 1, 0, 6)
print(seg_tree.query(1, arr, 1, 0, 6, 1, 3))


        


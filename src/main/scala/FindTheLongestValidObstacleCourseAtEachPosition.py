class Solution:
    def longestObstacleCourseAtEachPosition(self, obstacles: List[int]) -> List[int]:
        if not obstacles:
            return []
        lis = []
        res = [0] * len(obstacles)
        for i,x in enumerate(obstacles):
            if not lis or lis[-1] < x:
                lis.append(x)
                res[i] = len(lis)
            else:
                #replace subsequence with less value
                j = bisect.bisect_right(lis, x)
                if j == len(lis):
                    lis.append(x)
                else:
                    lis[j] = x
                res[i] = j + 1
        return res


class MaxBIT:
    def __init__(self, size):
        self.tree = [0] * (size + 1)

    def get(self, i):
        max_val = 0
        while i > 0:
            max_val = max(self.tree[i], max_val)
            i -= i & (-i)
        return max_val

    def update(self, i, a):
        while i < len(self.tree):
            self.tree[i] = max(self.tree[i], a)
            i += i & (-i)


class Solution:
    def longestObstacleCourseAtEachPosition(self, obstacles: List[int]) -> List[int]:
        if not obstacles:
            return []

        def compress(arr):
            # sorted uniq values
            uniq = sorted(set(arr))
            for i in range(len(arr)):
                # set up the how many items being before arr[i] plus 1
                arr[i] = bisect.bisect_left(uniq, arr[i]) + 1
            return len(uniq)

        uniqLen = compress(obstacles)
        # bit stores max length of sequences for the index i
        bit = MaxBIT(uniqLen)
        res = []
        for x in obstacles:
            # get max sequence length for [0: x] plus 1 counting current item
            subLen = bit.get(x) + 1
            res.append(subLen)
            # update max value for [x : uniqLen + 1]
            bit.update(x, subLen)
        return res
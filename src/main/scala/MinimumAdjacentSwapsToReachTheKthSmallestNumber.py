class Solution:
    def getMinSwaps(self, num: str, k: int) -> int:
        #  assert self._getMinSwaps('12',1) == 1,'test0' #21
        #  assert self._getMinSwaps('2133',2) == 2,'test1' #3213
        #  assert self._getMinSwaps('099',2) == 2,'test2' #990
        #  assert self._getMinSwaps('6975', 8) == 4,'test3'
        return self._getMinSwaps(num, k)

    def _getMinSwaps(self, num, k):

        def reverse_from(cur_num, s):
            e = len(cur_num) - 1
            while s < e:
                cur_num[s], cur_num[e] = cur_num[e], cur_num[s]
                s += 1
                e -= 1

        def make_perm(cur_num):
            # go from right
            # digits will be in decreasing order,otherwise swap right digits with left ones
            for i in range(len(cur_num) - 1, 0, -1):
                # if right i > left item
                if cur_num[i - 1] < cur_num[i]:
                    # swap from i to end of cur_num
                    reverse_from(cur_num, i)
                    # get bigger num,
                    # go from left to right
                    for j in range(i, len(cur_num)):
                        # find right that is greater then i-1,swap them
                        if cur_num[j] > cur_num[i - 1]:
                            cur_num[j], cur_num[i - 1] = cur_num[i - 1], cur_num[j]
                            return
            reverse_from(cur_num, 0)

        perm = list(num)
        # make k permutations
        for _ in range(k):
            make_perm(perm)
        cur_num = list(num)
        swaps = 0
        for i in range(len(perm)):
            if cur_num[i] != perm[i]:
                for j in range(i + 1, len(cur_num)):
                    if cur_num[i] == perm[j]:
                        swaps += j - i
                        perm = perm[:i + 1] + perm[i:i + j - i] + perm[j + 1:]
                        break
        return swaps

class Solution:
    def getMinSwaps(self, num: str, k: int) -> int:
        #  assert self._getMinSwaps('12',1) == 1,'test0' #21
        #  assert self._getMinSwaps('2133',2) == 2,'test1' #3213
        #  assert self._getMinSwaps('099',2) == 2,'test2' #990
        #  assert self._getMinSwaps('6975', 8) == 4,'test3'
        return self._getMinSwaps(num, k)

    def _getMinSwaps(self, num, k):

        def reverse(cur_num, s):
            e = len(cur_num) - 1
            while s < e:
                cur_num[s], cur_num[e] = cur_num[e], cur_num[s]
                s += 1
                e -= 1

        def find_next(cur_num):
            for i in range(len(cur_num) - 1, 0, -1):
                if cur_num[i] > cur_num[i - 1]:
                    reverse(cur_num, i)
                    for j in range(i, len(cur_num)):
                        if cur_num[j] > cur_num[i - 1]:
                            cur_num[j], cur_num[i - 1] = cur_num[i - 1], cur_num[j]
                            return
            reverse(cur_num, 0)

        kth_num = list(num)
        for _ in range(k):
            find_next(kth_num)
        swaps = 0
        num = list(num)
        for i in range(len(kth_num)):
            j = i

            while kth_num[i] != num[j]:
                j += 1
            while i < j:
                num[j - 1], num[j] = num[j], num[j - 1]
                swaps += 1
                j -= 1
        return swaps

sol = Solution()
print(sol.getMinSwaps("5489355142", 4))
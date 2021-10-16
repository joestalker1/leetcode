from math import inf

class Solution:
    def getMinSwaps(self, num: str, k: int) -> int:
      #  assert self._getMinSwaps('12',1) == 1,'test0' #21
      #  assert self._getMinSwaps('2133',2) == 2,'test1' #3213
      #  assert self._getMinSwaps('099',2) == 2,'test2' #990
        return self._getMinSwaps(num, k)

    def _getMinSwaps(self, num, k):

        def find_min_max_digits(cur_num):
            l = -1
            for i in range(len(cur_num) - 2, -1, -1):
                l = i + 1
                for j in range(i + 1, len(cur_num)):
                    if cur_num[j] > cur_num[i] and cur_num[j] < cur_num[l]:
                        l = j
                if cur_num[l] > cur_num[i]:
                    break
            return [i, l]

        dig_lst = list(num)
        cur_num = num
        swaps = 0
        for i in range(k):
            l, j = find_min_max_digits(dig_lst)
            dig_lst[l], dig_lst[j] = dig_lst[j], dig_lst[l]
            rest = dig_lst[l + 1:]
            rest.reverse()
            # revers s[l + 1:]
            dig_lst = dig_lst[0:l + 1] + rest
            # count swaps if possible
            diff = 0
            i = 0
            while i < len(dig_lst):
                if dig_lst[i] == cur_num[i]:
                    i += 1
                    continue
                elif dig_lst[i] == cur_num[i + 1] and dig_lst[i + 1] == cur_num[i]:
                    diff += 1
                    i += 2
                else:
                    diff = inf
                    break
            if diff == 1:
                swaps += 1
                cur_num = dig_lst[::]
        return swaps


sol = Solution()
print(sol.getMinSwaps("5489355142",4))#2
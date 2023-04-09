class Solution:
    def canThreePartsEqualSum(self, arr) -> bool:
        # assert self._canThreePartsEqualSum([0,2,1,-6,6,-7,9,1,2,0,1]), 'test1'
        # assert self._canThreePartsEqualSum([0,2,1,-6,6,7,9,-1,2,0,1]) == False, 'test2'
        # assert self._canThreePartsEqualSum([3,3,6,5,-2,2,5,1,-9,4]) == True,'test3'
        return self._canThreePartsEqualSum(arr)

    def _canThreePartsEqualSum(self, arr) -> bool:
        if not arr:
            return True
        arr_sum = sum(arr)
        part_sum = arr_sum // 3
        cnt = 0
        cur_sum = 0
        for num in arr:
            cur_sum += num
            if cur_sum == part_sum:
                cnt += 1
                cur_sum = 0
        return cnt >= 3 and arr_sum % 3 == 0
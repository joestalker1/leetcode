class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        assert self._findClosestElements([1, 2, 3], 3, 1) == [1, 2, 3], 'ascending array'
        assert self._findClosestElements([], 3, 1) == [], 'empty array'
        assert self._findClosestElements([1, 2, 3], 3, 5) == [1, 2, 3], 'x is max value'
        assert self._findClosestElements([10, 12, 13], 3, 5) == [10, 12, 13], 'x is min value'
        assert self._findClosestElements([1, 2, 3, 4, 5], 4, -1) == [1, 2, 3, 4], 'x is negative'
        return self._findClosestElements(arr, k, x)

    def _findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        if not arr or len(arr) <= k:
            return arr

        def find_closest(arr, k, x):
            s = 0
            e = len(arr) - k
            while s < e:
                m = s + (e - s) // 2
                r = m + k
                # compare x with (arr[m]+arr[m+k])//2
                if (arr[m] + arr[m + k]) // 2 < x:
                    s = m + 1
                # if x - arr[m] > arr[r] - x:
                # go to right
                #   s = m + 1
                else:
                    e = m
            return s

        # find low boundey for k range
        i = find_closest(arr, k, x)

        return arr[i:i + k]








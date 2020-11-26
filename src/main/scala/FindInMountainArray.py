class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        n = mountain_arr.length()
        if n < 3:
            return -1
        peak = self.find_peak(mountain_arr, 0, n - 1)
        if peak == -1:
            return peak
        left = self.find_target(mountain_arr, target, 0, peak, True)
        if left != -1:
            return left
        return self.find_target(mountain_arr, target, peak, n - 1, False)

    def find_peak(self, arr, s, e):
        while s < e:
            m = s + (e - s)//2
            a = arr.get(a)
            if a < arr.get(m+1):
                s = m + 1
            else:
                e = m
        return e

    def find_target(self, arr, target, s, e, asc):
        while s <= e:
            m = s + (e - s)//2
            a = arr.get(m)
            if a == target:
                return m
            if asc:
                if a < target:
                    s = m + 1
                else:
                    e = m - 1
            else:
                if a < target:
                    e = m - 1
                else:
                    s = m + 1
        return -1

class MountainArray:
    def __init__(self, arr):
        self.arr = arr


    def get(self, index: int):
        return self.arr[index]

    def length(self):
        return len(self.arr)


class Solution:
    def find_peak(self, mountain_arr: 'MountainArray',s, e):
        while s < e:
            m = s + (e - s) // 2
            a = mountain_arr.get(s)
            b = mountain_arr.get(e)
            if a <= b:
                s = m + 1
            else:
                e = m - 1
        return s

    def find_inc(self,mountain_arr: 'MountainArray', x, s, e):
        while s < e:
            m = s + (e - s)//2
            a = mountain_arr.get(m)
            if a == x:
                return m
            if a > x:
                e = m - 1
            else:
                s = m + 1
        return s

    def find_dec(self,mountain_arr: 'MountainArray', x, s, e):
        while s < e:
            m = s + (e - s)//2
            a = mountain_arr.get(m)
            if a == x:
                return m
            if a > x:
                s = m + 1
            else:
                e = m - 1
        return s

    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        n = mountain_arr.length()
        p = self.find_peak(mountain_arr, 0, n-1)
        i = self.find_inc(mountain_arr, target, 0, p)
        a = mountain_arr.get(i)
        if a == target:
            return i
        i = self.find_dec(mountain_arr,target, p, n-1)
        a = mountain_arr.get(i)
        return i if a == target else -1



sol = Solution()

m = MountainArray([3,5,3,2,0])
print(sol.findInMountainArray(5, m))#1

m = MountainArray([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,100,99,98,97,96,95,94,93,92,91,90,89,88,87,86,85,84,83,82])
print(sol.findInMountainArray(101, m))


m = MountainArray([3,5,3,2,0])
print(sol.findInMountainArray(3, m))

m = MountainArray([1,5,2])
print(sol.findInMountainArray(2, m))

m = MountainArray([1,2,3,5,4,3,1])
print(sol.findInMountainArray(2, m))

m = MountainArray([0,1,2,4,2,1])
print(sol.findInMountainArray(3, m))#-1

m = MountainArray([1,2,3,4,5,3,1])
print(sol.findInMountainArray(3, m))

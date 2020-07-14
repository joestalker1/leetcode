class Solution:
    def findAllTriplets(self,arr):
        if len(arr) < 3:
            return []
        arr.sort()
        res = []

        def find_num(a, arr, s, e):
            if s > e:
                return -1
            while s <= e:
                mid = s + (e - s) // 2
                if arr[mid] == a:
                    return mid
                if arr[mid] > a:
                    e = mid -1
                else:
                    s = mid + 1
            return -1

        for i in range(len(arr)):
            a = arr[i]
            target = 0 - a
            for j in range(i+1, len(arr)):
                b = arr[j]
                k = find_num(target - b, arr, j+1, len(arr)-1)
                if k != -1:
                    res.append([a,b,arr[k]])
        return res


sol = Solution()
print(sol.findAllTriplets([0, -1, 2, -3, 1]))




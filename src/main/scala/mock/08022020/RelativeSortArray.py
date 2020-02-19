class Solution:
    def relativeSortArray(self, arr1, arr2):
        m = {x:i for i,x in enumerate(arr2)}
        def arr_key(x):
            return m[x] if x in m else x
        arr1.sort(key=arr_key)
        return arr1


sol = Solution()
print(sol.relativeSortArray(arr1 = [2,3,1,3,2,4,6,7,9,2,19], arr2 = [2,1,4,3,9,6]))
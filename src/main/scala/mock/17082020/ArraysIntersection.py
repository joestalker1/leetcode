class Solution:
    def arraysIntersection(self, arr1, arr2, arr3):
        if not arr1 or not arr2 or not arr3:
            return []

        def merge(arr1, arr2):
            res = []
            i1 = 0
            i2 = 0
            while i1 < len(arr1) and i2 < arr2:
                a = arr1[i1]
                b = arr2[i2]
                if a == b:
                    res.append(a)
                    i1 += 1
                    i2 += 1
                else:
                    if a > b:
                        i2 += 1
                    else:
                        i1 += 1
            return res

        return merge(merge(arr1, arr2), arr3)

class Solution:
    def countInversion(self, arr):
        tmp = [0] * len(arr)

        def merge(arr, tmp, l, mid,r):
            i = l
            j = mid+1
            k = l
            pair = 0
            while i <= mid and j <= r:
                if arr[i] <= arr[j]:
                    tmp[k] = arr[i]
                    i += 1
                else:
                    pair += (mid - i + 1)
                    tmp[k] = arr[j]
                    j += 1
                k += 1
            while i <= mid:
                tmp[k] = arr[i]
                i += 1
                k += 1
            while j <= r:
                tmp[k] = arr[j]
                j += 1
                k += 1
            for i in range(l,r+1):
                arr[i] = tmp[i]
            return pair

        def split(arr, tmp, l, r):
            pair = 0
            if l < r:
                mid = l + (r - l) //2
                pair += split(arr, tmp, l, mid)
                pair += split(arr, tmp, mid+1, r)
                pair += merge(arr, tmp, l,mid, r)
            return pair

        return split(arr, tmp,0,len(arr) - 1)
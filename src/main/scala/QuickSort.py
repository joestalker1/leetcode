def parition(arr, lo, hi):
    p = arr[hi]
    j = lo
    for i in range(lo, hi):
        if arr[i] < p:
            arr[i],arr[j] = arr[j],arr[i]
            j += 1
    arr[hi],arr[j] = arr[j], arr[hi]
    return p



def quick_sort(arr, lo, hi):
    if lo < hi:
        pivot = parition(arr, lo, hi)
        quick_sort(arr, lo, pivot - 1)
        quick_sort(arr, pivot + 1, hi)

arr = [2, -3, 4, 9, 0]
quick_sort(arr, 0, len(arr) - 1 )
print(arr)
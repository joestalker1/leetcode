def kthSmallest(arr, k, lo, hi):
    pivot = partition(arr, lo, hi)
    if pivot == k:
        return arr[k]
    if pivot > k:
        return kthSmallest(arr, k, lo, pivot - 1)
    return kthSmallest(arr, k, pivot + 1, hi)

def partition(arr, lo, hi):
    p = arr[hi]
    i = lo - 1
    for j in range(lo, hi):
        if p > arr[j]:
            i += 1
            arr[i],arr[j]=arr[j],arr[i]
    arr[i+1],arr[hi] = arr[hi],arr[i+1]
    return i + 1


print(kthSmallest([5,5,5], 0, 0, 2))




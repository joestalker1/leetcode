import random


def part(arr, l, r):
    p = random.randint(l, r)
    arr[r], arr[p] = arr[p], arr[r]
    i = l
    j = l
    lst = arr[r]
    while j < r:
        if arr[j] < lst:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
        j += 1
    arr[i], arr[r] = arr[r], arr[i]
    return i


def get_median(arr, k, l, r, ab):
    if l <= r:
        p = part(arr, l, r)
        if p == k:
            ab[1] = arr[p]
            if ab[0] != -1:
                return
        elif p == k - 1:
            ab[0] = arr[p]
            if ab[1] != -1:
                return
        elif p >= k:
            return get_median(arr, k, l, p - 1, ab)
        else:
            return get_median(arr, k, p + 1, r, ab)


ab = [-1, -1]
arr = [12, 3, 5, 7, 4, 26]
n = len(arr)

if n % 2 == 1:
    get_median(arr, n // 2, 0, n - 1, ab)
    print(ab[1])
else:
    get_median(arr, n // 2, 0, n - 1, ab)
    print((ab[0] + ab[1]) // 2)

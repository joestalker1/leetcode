comp = 0

def partition(arr, start, end, diff):
    global comp
    pivot = arr[end]
    i = start - 1
    for j in range(start, end):
        #if arr[j] <= pivot:
        if abs(arr[j] - pivot) > diff:
            i += 1
            #if abs(arr[j] - pivot) <= diff:
               # print("{},{}".format(arr[j], pivot))
            comp += 1
            arr[i], arr[j] = arr[j],arr[i]
        # else:
        #     if abs(arr[j] - pivot) <= diff:
        #         #print("{},{}".format(arr[j], pivot))
        #         comp += 1


    arr[i + 1], arr[end] = arr[end], arr[i + 1]
    return i + 1


def quicksort(arr, start, end, diff):
    if start < end:
        pivot = partition(arr, start, end, diff)
        quicksort(arr, start, pivot - 1, diff)
        quicksort(arr, pivot + 1, end, diff)





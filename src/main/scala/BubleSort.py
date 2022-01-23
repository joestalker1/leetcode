def buble_sort(arr):
    for it in range(1,len(arr)):
        for j in range(len(arr) - it):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
    return arr


print(buble_sort([6,5,4,3,2,1,0]))


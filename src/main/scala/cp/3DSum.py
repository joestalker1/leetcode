def findSumFor2(arr, sum1):
    i = 0
    j = len(arr)-1
    while(i < j):
        if arr[i] + arr[j] > sum1:
            j-= 1
        elif arr[i] + arr[j] < sum1:
            i+=1
        else:
            return [i, j]
    return [i, j]

def findSumFor3(arr, sum1):
    sorted_arr = sorted(arr)
    for i in range(0, len(arr)):
        x = arr[i]
        res = findSumFor2(arr[i+1:], -x)
        if res[0] != res[1]:
            return [i, res[0], res[1]]
    return None

print(findSumFor3([4, 3, -1, 2, -2, 10], 4))
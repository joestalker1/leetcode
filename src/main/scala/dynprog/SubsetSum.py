def isSubarrSum(arr, x):
    mat = [0] * (x + 1)
    n = len(arr)
    for i in range(len(mat)):
        mat[i] = [0] * (len(arr) + 1)
    for i in range(len(mat[0])):
        mat[0][i] = True
    for i in range(1, x + 1):
        mat[i][0] = False
    for i in range(1, x + 1):
        for j in range(1, n + 1):
            mat[i][j] = mat[i][j-1]
            if i >= arr[j-1]:
                mat[i][j] = mat[i][j] or mat[i - arr[j-1]][j - 1]
    return mat[x][n]

#print(isSubarrSum([3,2,7,1],60))

def bin_search(arr, x):
    s = 0
    e = len(arr) - 1
    while s <= e:
        m = s + (e - s) // 2
        if arr[m] == x:
            return True
        if arr[m] > x:
            e = m - 1
        else:
            s = m + 1
    return False


def question9_7(arr, x):
    if not arr:
        return []
    arr = sorted(arr)
    for i in range(len(arr)):
        b = x - arr[i]
        if bin_search(arr, b):
            return [arr[i], b]
    return []
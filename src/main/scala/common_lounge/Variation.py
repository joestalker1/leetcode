def find_pairs(arr, diff):
    pairs = 0
    i = 0
    j = 0
    while i < len(arr) and j < len(arr):
        while j < len(arr) and abs(arr[j] - arr[i]) < diff:
            j += 1
        if j < len(arr):
            pairs += (len(arr) - j)
        i += 1
    return pairs


s = input()
arr = s.split()
n = int(arr[0])
k = int(arr[1])
s = input()
arr = s.split()
#arr = [3,1,3]
#k = 1
arr = list([int(a) for a in arr])
arr.sort()
print(find_pairs(arr, k))

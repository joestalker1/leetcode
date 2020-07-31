def powersets(arr):
    if not arr:
        return []
    res = []

    def backtrack(res, buf, start):
        res.append(buf[::])
        for i in range(start, len(arr)):
            buf.append(arr[i])
            backtrack(res, buf, i + 1)
            buf.pop(-1)

    backtrack(res, [], 0)
    return res

def permutations(arr):
    res = []

    def backtrack(res, buf, start):
        if len(buf) == len(arr):
            res.append(buf[::])
            return
        if start == len(arr):
            return
        arr[0], arr[start] = arr[start], arr[0]
        for i in range(start, len(arr)):
            buf.append(arr[i])
            backtrack(res, buf, i+1)
            buf.pop(-1)
        arr[0], arr[start] = arr[start], arr[0]

    backtrack(res, [], 0)
    return res



print(permutations([1,2,3]))
#print(powersets([1,2,3]))
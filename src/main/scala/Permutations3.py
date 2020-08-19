def permutations(arr):
    res = []

    def backtrack(start, res):
        if start == len(arr):
            res.append(arr[::])
            return
        for i in range(start, len(arr)):
            arr[start],arr[i] = arr[i],arr[start]
            backtrack(start + 1, res)
            arr[start], arr[i] = arr[i], arr[start]

    backtrack(0, res)
    return res

def perm_no_dup(arr):
    res = []
    arr.sort()
    def backtrack(res, temp, used):
        if len(temp) == len(arr):
            res.append(temp[::])
            return
        for i in range(len(arr)):
            if i in used or i > 0 and arr[i] == arr[i-1] and (i-1) not in used:
                continue
            temp.append(arr[i])
            used.add(i)
            backtrack(res, temp, used)
            used.discard(i)
            temp.pop(-1)

    backtrack(res, [], set())
    return res


print(perm_no_dup([1,2,3]))



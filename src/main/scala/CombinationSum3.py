def comb_sum(arr, target):
    arr.sort()
    res = []

    def backtrack(res, temp, remain, start):
        if remain < 0:
            return
        if remain == 0:
            res.append(temp[::])
            return
        for i in range(start, len(arr)):
            temp.append(arr[i])
            backtrack(res, temp, remain - arr[i], i)
            temp.pop(-1)

    backtrack(res, [], target, 0)
    return res


def comb_sum_no_dup(arr, target):
    arr.sort()
    res = []

    def backtrack(res, temp, remain, start):
        if remain < 0:
            return
        if remain == 0:
            res.append(temp[::])
            return
        for i in range(start, len(arr)):
            if i > start and arr[i] == arr[i-1]:
                continue
            temp.append(arr[i])
            backtrack(res, temp, remain - arr[i], i+1)
            temp.pop(-1)

    backtrack(res, [], target, 0)
    return res


print(comb_sum_no_dup([2,3,6,7], 7))
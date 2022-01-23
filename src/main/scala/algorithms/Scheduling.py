def schedule(arr):
    if not arr:
        return None
    sorted_arr = sorted(arr,key= lambda x: x[1])
    res = []
    for i in range(0, len(sorted_arr)):
        if i == 0:
            res.append(sorted_arr[i])
        elif res[len(res)-1][1] <= sorted_arr[i][0]:
            res.append(sorted_arr[i])
    return res


print(schedule([[1,3], [2,5],[3,9], [6,8]]))
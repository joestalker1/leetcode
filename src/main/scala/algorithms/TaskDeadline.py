def taskDeadline(arr):
    if not arr:
        return None
    sorted_arr = sorted(arr,key= lambda x: x[0])
    expenses = 0
    x = 0
    for i in range(0, len(sorted_arr)):
        x += sorted_arr[i][0]
        expenses += (sorted_arr[i][1] - x)

    return expenses


print(taskDeadline([[4,2],[3,5],[2,7],[4,5]]))
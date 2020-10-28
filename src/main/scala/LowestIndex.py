def lowest_index_val(lst):
    result = None
    left, right = 0, len(lst) - 1
    while left <= right:
        mid = (left + right) // 2
        if lst[mid] == mid:
            result = mid
            right = mid - 1
        elif lst[mid] < mid:
            left = mid + 1
        else:
            right = mid - 1

    return result


print(lowest_index_val([-5, -3, 2, 3]))
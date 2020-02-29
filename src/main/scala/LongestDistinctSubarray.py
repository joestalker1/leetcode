def distinct_subarray(arr):
    d = {} # most recent occurrences of each element
    result = 0
    longest_distinct_subarray_start_index = 0
    for i, e in enumerate(arr):
        if e in d:
            # If d[e] appears in the middle of the current longest distinct subarray
            if d[e] >= longest_distinct_subarray_start_index:
                result = max(result, i - longest_distinct_subarray_start_index)
                longest_distinct_subarray_start_index = d[e] + 1
        d[e] = i

    return max(result, len(arr) - longest_distinct_subarray_start_index)


print(distinct_subarray( [5, 1, 3, 5, 2, 3, 4, 1]))
def largest_consecutive_range(arr):
    nums = set(arr)
    longest_range = (0, 0)
    for num in nums:
        # check if num is range already if nums - 1 is in arr
        if num - 1 not in nums:
            # find upper bound of range
            curr = num + 1

            while curr in nums:
                curr += 1
            # get maximum range
            if curr - num > longest_range[1] - longest_range[0]:
                longest_range = (num, curr - 1)
    return longest_range


print(largest_consecutive_range([9, 6, 1, 3, 8, 10, 12, 11]))
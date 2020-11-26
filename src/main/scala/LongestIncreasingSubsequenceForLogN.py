import bisect


def longest_increasing_subsequence_length(nums):
    sorted_nums = []
    for n in nums:
        index = bisect.bisect_left(sorted_nums, n)
        if index == len(sorted_nums):  # If larger than all elements,
            sorted_nums.append(n)      # Extend the sorted list.
        else:
            # prefer smaller item to get longer subsequence
            sorted_nums[index] = n     # Replace the next-largest number.

    return len(sorted_nums)


print(longest_increasing_subsequence_length([10, 9, 2, 5, 3, 7, 101, 18]))
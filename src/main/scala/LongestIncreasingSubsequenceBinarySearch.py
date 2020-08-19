import bisect

def longest_increasing_subsequence_length(nums):
    sorted_nums = []
    for n in nums:
        # find position to insert new n
        index = bisect.bisect_left(sorted_nums, n)
        # if larger then all ellements, extend sorted_nums
        if index == len(sorted_nums):  # If larger than all elements,
            sorted_nums.append(n)      # Extend the sorted list.
        else:                          # Otherwise,
            # assign sorted_nums[index] = n by lesser value
            sorted_nums[index] = n     # Replace the next-largest number.

    return len(sorted_nums)

print(longest_increasing_subsequence_length([10, 9, 2, 5, 3, 7, 101, 18]))
from math import ceil, floor


def round_numbers(array):
    # find lower sum value
    result = [floor(x) for x in array]
    # calculate difference between desired sum and lower one
    leftover = int(round(sum(array)) - sum(result))
    # sort array in increasing difference between current value - floored value
    diffs = sorted(enumerate(array), key=lambda x: x[1] - floor(x[1]))
    # distribute leftover over result values
    while leftover > 0:
        result[diffs.pop()[0]] += 1
        leftover -= 1

    return result


print(round_numbers([1.3, 2.3, 4.4]))

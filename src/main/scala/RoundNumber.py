from math import floor


def round_numbers(array):
    result = [floor(x) for x in array]

    leftover = int(round(sum(array)) - sum(result))
    # sort by increasing diff array[i] and round down array[i]
    diffs = sorted(enumerate(array), key=lambda x: x[1] - floor(x[1]))

    while leftover > 0:
        # take item with max diff array[i] and round down array[i]
        result[diffs.pop()[0]] += 1
        leftover -= 1

    return result

print(round_numbers([1.3, 2.3, 4.4]))
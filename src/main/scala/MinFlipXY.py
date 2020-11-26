def num_flips(string):
    n = len(string)
    y_left = [0] * n
    x_right = [0] * n

    l, r = 0, 0
    for i in range(n):
        y_left[i] = l
        if string[i] == 'y':
            l += 1

    for i in range(n - 1, -1, -1):
        x_right[i] = r
        if string[i] == 'x':
            r += 1

    return min(sum(pair) for pair in zip(y_left, x_right))


print(num_flips("xyxxxyxyy"))
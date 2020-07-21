def apply_ops(a, b):
    return [a + b, a - b, a * b, a / b]


def calc_exp(arr, a):
    if len(arr) == 1:
        return arr[0] == a
    elif len(arr) == 2:
        return any(calc_exp([x], a) for x in apply_ops(*arr))
    else:
        for i in range(len(arr) - 2):
            for x in apply_ops(*arr[i:i+2]):
                if calc_exp(arr[:i] + [x] + arr[i+2:], a):
                    return True
        return False


print(calc_exp([5, 2, 7, 8], 24))


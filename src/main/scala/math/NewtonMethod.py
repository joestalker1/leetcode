def square_root(s):
    x = 10
    while abs(s - x * x) > 0.0000001:
        x = x - (x * x - s) / (2 * x)
    return x


print(square_root(10))

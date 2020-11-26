def min_squares(n):
    perfect_squares = []
    for i in range(1, int(n ** 0.5) + 1):
        if i * i <= n:
            perfect_squares.append(i * i)

    min_squares = [i for i in range(n + 1)]

    for i in range(2, n + 1):
        for p in perfect_squares:
            if i - p >= 0:
                min_squares[i] = min(min_squares[i], 1 + min_squares[i - p])

    return min_squares[-1]


print(min_squares(18))
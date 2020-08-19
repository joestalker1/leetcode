def min_squares(n):
    perfect_squares = []
    #find number = a * a
    for i in range(1, int(n ** 0.5) + 1):
        if i * i <= n:
            perfect_squares.append(i * i)
    # initialy all are i as maximum value
    min_squares = [i for i in range(n + 1)]

    for i in range(2, n + 1):
        # if i - p is perfect square then result = min(min_squares[i], 1 + number of perfect square for (i-p))
        for p in perfect_squares:
            min_squares[i] = min(min_squares[i], 1 + min_squares[i - p])

    return min_squares[-1]

print(min_squares(10))


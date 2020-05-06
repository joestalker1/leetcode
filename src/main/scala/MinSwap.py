def min_swaps(row):
    n = len(row)

    positions = [0 for i in range(n)]
    for i in range(n):
        positions[row[i]] = i

    swaps = 0

    for i in range(0, n, 2):
        if row[i] // 2 == row[i + 1] // 2:
            continue

        if row[i] % 2 == 0:
            partner = positions[row[i] // 2 * 2 + 1]
        else:
            partner = positions[row[i] // 2 * 2]

        row[i + 1], row[partner] = row[partner], row[i + 1]
        swaps += 1

    return swaps

print(min_swaps([(0, 4), (1, 3), (2, 5)]))
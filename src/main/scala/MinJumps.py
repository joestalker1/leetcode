def min_jumps(arr):
    moves = [float("inf") for _ in range(len(arr) - 1)] + [0]

    for i in range(len(arr) - 1, -1, -1):
        if arr[i] != 0:
            for jump in range(i + 1, min(i + 1 + arr[i], len(arr))):
                moves[i] = min(moves[i], 1 + moves[jump])

    return moves[0]

print(min_jumps([6, 2, 4, 0, 5, 1, 1, 4, 2, 9]))
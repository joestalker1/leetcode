def dropngEggs(numFloors, numEggs):
    if numFloors == 1 or numFloors == 0 or numEggs == 1:
        return numFloors
    min1 = float("inf")
    for p in range(1, numFloors + 1):
        temp = max(dropngEggs(p-1, numEggs), dropngEggs(numFloors - p, numEggs))
        if temp < min1:
            min1 = temp
    return min1 + 1

print(dropngEggs(10, 2))


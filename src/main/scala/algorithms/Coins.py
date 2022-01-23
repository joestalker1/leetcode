def coinSum(x, coins):
    if x <= 0:
        return 0
    vals = [0] * (x + 1)
    for i in range(1, x + 1):
        vals[i] = float("inf")
        for c in coins:
            if i - c >= 0:
                vals[i] = min(vals[i], 1 + vals[i - c])

    return vals[x]


def coinSumSolution(x, coins):
    if x <= 0:
        return 0
    first = [0] * (x + 1)
    vals = [0] * (x + 1)
    for s in range(1, x + 1):
        vals[s] = float("inf")
        for c in coins:
            if s - c >= 0 and vals[s] > vals[s - c]:
                vals[s] = 1 + vals[s - c]
                first[s] = c
    return first

def printSol(x, first):
    while x > 0:
        print(first[x])
        x -= first[x]

def coinWays(x, coins):
    if x <= 0:
        return 0
    ways = [0] * (x + 1)
    ways[0] = 1
    for s in range(1, x + 1):
        for c in coins:
            if s - c >= 0:
                ways[s] += ways[s - c]
    return ways[x]

print(coinWays(5, [1,3,4]))
#printSol(200, sol)


#print(coinSum(120, [1,5,10,25,50]))

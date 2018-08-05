def countWays(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n == 2:
        return 2
    return countWays(n - 1) + countWays(n - 2)

def countWays3(n):
    if n < 0 or n % 2 != 0:
        return 0
    if n == 2:
        return 2
    if n == 4:
        return 2
    return countWays3(n - 2) + countWays3(n - 4)


print(countWays3(8))


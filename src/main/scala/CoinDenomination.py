def coin_change_dp(denominations, total):
    cache = [float('inf') for _ in range(total + 1)]

    for d in denominations:
        if d < len(cache):
            cache[d] = 1

    for i in range(1, total + 1):
        for d in denominations:
            if i - d >= 0:
                cache[i] = min(cache[i - d] + 1, cache[i])

    if cache[total] == float('inf'):
        return None
    return cache[total]


print(coin_change_dp([5, 8], 15))
print(coin_change_dp([1, 5, 10], 56))
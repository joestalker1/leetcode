def array_two_elements(arr):
    xor = 0
    for num in arr:
        xor = xor ^ num

    # Get rightmost set bit
    xor = xor & -xor

    rets = [0, 0]
    for num in arr:
        if num & xor:
            rets[0] = rets[0] ^ num
        else:
            rets[1] = rets[1] ^ num
    return rets


print(array_two_elements([2, 4, 6, 8, 10, 2, 6, 10]))
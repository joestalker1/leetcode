def get2NonRepeatingNos(arr):
    xor = arr[0]
    for i in range(1, len(arr)):
        xor = xor ^ arr[i]

    rightmost_bit = xor & ~ (xor - 1)
    x1 = 0
    y1 = 0
    for i in range(len(arr)):
        if arr[i] & rightmost_bit:
            x1 = x1 ^ arr[i]
        else:
            y1 = y1 ^ arr[i]
    return [x1, y1]

print(get2NonRepeatingNos([2, 4, 7, 9, 2, 4]))

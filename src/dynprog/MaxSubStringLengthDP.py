def maxSubStringLength(s):
    if not s or len(s) == 0:
        return 0
    n = len(s)
    max_len = 0
    for l in range(2, len(s) + 1):
        mem = [0] * (2 * (n + 1))
        for i in range(len(s)):
            mem[i + i] = int(s[i]) - int('0')
        for i in range(0, len(s) - l + 1):
            j = i + l - 1
            k = l // 2
            mem[i+j] = mem[i + j - k] + mem[j - k + 1 + j]
            if l % 2 == 0 and mem[i + j - k] == mem[j - k + 1+ j] and l > max_len:
                max_len = l
    return max_len


print(maxSubStringLength("9430723"))


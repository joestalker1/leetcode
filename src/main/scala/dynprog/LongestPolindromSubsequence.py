def longPoliSub(s):
    if not s or len(s) == 0:
        return 0
    table = [0] * (len(s) + 1)
    for i in range(0, len(s) + 1):
        table[i] = [0] * (len(s) + 1)

    for i in range(i, len(s)):
        table[i][i] = 1

    for k in range(2, len(s) + 1):
        for i in range(0, len(s) - k + 1):
            j = i + k - 1
            if s[i] == s[j] and k == 2:
                table[i][j] = 2
            elif s[i] == s[j]:
                table[i][j] = table[i+1][j-1] + 2
            else:
                table[i][j] = max(table[i][j-1], table[i+1][j])
    return table[0][len(s) - 1]

print(longPoliSub("BBABCBCAB"))

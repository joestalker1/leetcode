def lcs(str1, str2):
    m = len(str1)
    n = len(str2)
    lcs_count = [0] * (m + 1)
    lcs_count = [[0]*(n + 1) for l in lcs_count]
    for i in range(m+1):
        lcs_count[i][0] = 0

    for j in range(n + 1):
        lcs_count[0][j] = 0

    for i in range(1,m + 1):
        for j in range(1, n + 1):
            if str1[i-1] == str2[j-1]:
                lcs_count[i][j] = 1 + lcs_count[i-1][j-1]
            else:
                lcs_count[i][j] = max(lcs_count[i-1][j], lcs_count[i][j-1])
    return lcs_count[m][n]

print(lcs("ABCD","AEBD"))



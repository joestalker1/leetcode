def editDistance(s1,s2):
    if not s1 and not s2:
        return 0
    if not s1:
        return len(s2)
    if not s2:
        return len(s1)
    edit = [0] * (len(s1) + 1)
    for i in range(len(edit)):
        edit[i] = [0] * (len(s2) + 1)
    for i in range(len(s2) + 1):
        edit[0][i] = i
    for i in range(len(s1)+1):
        edit[i][0] = i
    for i in range(1, len(s1)+1):
        for j in range(1, len(s2)+1):
            if s1[i-1] == s2[j-1]:
                edit[i][j] = edit[i-1][j-1]
            else:
                edit[i][j] = min(edit[i-1][j], edit[i][j-1], edit[i-1][j-1]) + 1

    return edit[len(s1)][len(s2)]


print(editDistance("catt", "carrt"))
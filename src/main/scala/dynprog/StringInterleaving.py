def is_interleaving(a, b, c):
    m = len(a)
    n = len(b)
    if len(c) != m + n:
        return False
    mat = [0] * (m + 1)
    for i in range(len(mat)):
        mat[i] = [0] * (n + 1)

    mat[0][0] = True

    for i in range(1, m + 1):
        if a[i - 1] != c[i - 1]:
            mat[i][0] = False
        else:
            mat[i][0] = mat[i - 1][0]

    for j in range(1, n + 1):
        if b[j - 1] != c[j - 1]:
            mat[0][j] = False
        else:
            mat[0][j] = mat[0][j - 1]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if a[i - 1] == c[i + j - 1] and b[j - 1] != c[i + j - 1]:
                mat[i][j] = mat[i - 1][j]
            elif a[i - 1] != c[i + j - 1] and b[j - 1] == c[i + j - 1]:
                mat[i][j] = mat[i][j - 1]
            elif a[i - 1] == c[i + j - 1] and b[j - 1] == c[i + j - 1]:
                mat[i][j] = mat[i-1][j] or mat[i][j-1]
            else:
                mat[i][j] = False
    return mat[m][n]

#print(is_interleaving("bbca", "bcc", "bbcbcac"))

def question95(a, b):
    if not a and not b:
        return ""
    if not a:
        return b
    if not b:
        return a
    def gen(chars, seq, result):
        if not len(chars):
            result.append(seq)
            return
        new_seq = seq[:]
        for i in range(len(chars)):
            new_seq.append(chars[i])
            new_chars = chars[0:i] + chars[i+1:]
            gen(new_chars, new_seq, result)
            new_seq = new_seq[:-1]
    res = []
    gen(a + b, [], res)
    return [''.join(seq) for seq in res]

print(question95("AB","C"))

# s1 and a2 have unique characters
def question96(s1, s2, s):
    m = len(s1)
    n = len(s2)
    if len(s) != m + n:
        return False
    i1 = 0
    i2 = 0
    for j in range(len(s)):
        if s[j] == s1[i1]:
            i1 += 1
        elif s[j] == s2[i2]:
            i2 += 1
        else:
            return False
    return True

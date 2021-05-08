def build(p):
    l = 0
    i = 1
    lps = [0] * len(p)
    while i < len(p):
        if p[i] == p[l]:
            l += 1
            lps[i] = l
            i += 1
        else:
            if l != 0:
                l = lps[l-1]
            else:
                i += 1
    return lps

def find(s, p):
    lps = build(p)
    i = 0
    j = 0
    while i < len(s):
        if s[i] == p[j]:
            i += 1
            j += 1
        if j == len(p)-1:
            return s[i-len(p)+1:]
        elif i < len(s) and s[i] != p[j]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
    return None

print(find("aaaaaabc", "abc"))
def is_poli(s, i):
    l = i -1
    r = i + 1
    while l >= 0 and r < len(s) and s[l] == '?' and s[r] == '?':
        l -= 1
        r += 1
    while l >= 0 and r < len(s) and s[l] == s[r] and s[l] != '?':
        l -= 1
        r += 1
    return (l+1,r-1) if s[l+1] != s[r - 1] and s[l+1] != '?' else None


def solve():
    t = int(input())
    for i in range(1, t + 1):
        s = input().strip()
        for i in range(len(s)):
            if s[i] == '?':
                #check if left and right are polindroms:
                (l,r) = is_poli(s, i):




solve()
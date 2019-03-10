def hashing(s, a, b, i, j):
    h = [0] * len(s)
    h[0] = ord(s[0])
    for i in range(1, len(s)):
        h[i] = (h[i - 1] * a + ord(s[i])) % b
    p = [0] * len(s)
    p[0] = 1
    for k in range(1, len(s)):
        p[k] = (p[k - 1] * a) % b
    return (h[i] - h[j - 1] * p[i - j + 1]) % b if j > 0 else h[i]


# s = "abcdef"
# print(hashing(s, 911382323, 972663749, len(s), 0))
# s = "abcdee"
# print(hashing(s, 911382323, 972663749, len(s), 0))

def fill_zarr(str, z):
    l = 0
    r = 0
    for i in range(1, len(str)):
        if i > r:
            l = r = i
            while r < len(str) and str[r - l] == str[r]:
                r += 1
            z[i] = r - l
            r -= 1
        else:
            k = i - r
            if z[k] < r - i + 1:
                z[i] = z[k]
            else:
                l = i
                while r < len(str) and str(r - l) == str(r):
                    r += 1
                z[i] = r - l
                r -= 1


def zalgorithm(s, sub):
    concat = sub + "$" + s
    z = [0] * len(concat)
    fill_zarr(concat, z)
    for i in range(0, len(concat)):
        if z[i] == len(sub):
            return True
    return False

print(zalgorithm("hattivatti", "att"))

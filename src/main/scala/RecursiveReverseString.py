def reverseString(s):
    if not s:
        return s
    return s[-1] + reverseString(s[:-1])

def rev_max(arr):
    if len(arr) == 1:
        return arr[0]
    return max(arr[0], rev_max(arr[1:]))

def rev_polidrom(arr):
    if len(arr) == 1:
        return True
    if arr[0] == arr[-1]:
        return rev_polidrom(arr[1:-1])
    return False

def rev_perm(arr):
    if len(arr) == 1:
        return [[arr[0]]]
    res = []
    for i in range(len(arr)):
        ch = arr[i]
        rem = arr[:i] + arr[i + 1:]
        perms = rev_perm(rem)
        for perm in perms:
            res.append([ch] + perm)
    return res


print(rev_perm(['a', 'b', 'c']))


print(rev_max([1,2,3,4]))
print(reverseString('covid'))
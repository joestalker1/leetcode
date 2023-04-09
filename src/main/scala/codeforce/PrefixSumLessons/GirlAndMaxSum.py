def solve():
    n,q = list(map(int, input().split()))
    arr = list(map(int, input().split()))
    freq = [0] * n
    qr = [0] * q
    for i in range(q):
        l,r = map(int,input().split())
        l -= 1
        freq[l] += 1
        if r < len(freq):
            freq[r] -= 1
        qr[i] = [l, r]
    for i in range(1,len(freq)):
        freq[i] += freq[i-1]
    index = [i for i in range(n)]
    index.sort(key=lambda x:freq[x])
    arr.sort(key=lambda x:-x)
    new_arr = [0] * n
    j = 0
    for i in index:
        new_arr[i] = arr[j]
        j += 1
    pr = [0] * (n + 1)
    j = 0
    for i in range(n):
        pr[i+1] = pr[i] + new_arr[i]
    total = 0
    for l,r in qr:
        total += pr[r] - pr[l]
    print(total)

solve()
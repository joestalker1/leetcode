def run_task():
    t = int(input().strip())
    for _ in range(t):
        n = int(input().strip())
        arr = input().strip().split(' ')
        arr = list(map(lambda x: int(x), arr))
        arr.sort()
        if len(arr) == 2:
            print(0)
            continue
        if len(arr) == 3:
            cost = min(abs(arr[0] - arr[1]), abs(arr[2] - arr[1]))
            print(cost)
            continue
        # if A is consist [0: arr[(n-1)/2]] or [arr[1+(n-1)/2]
        d1 = 0
        for i in range(n - 1):
            d1 += abs(arr[i] - arr[(n - 1) // 2])
        d2 = 0
        for i in range(1, n):
            d2 += abs(arr[i] - arr[1 + (n - 1) // 2])
        cost = min(d1, d2)
        l = 1
        r = len(arr) - 2
        # consider arr[l:n-2] and arr[0:r] and change r or l, we cang neglect the rest of array items
        while l < r:
            d2 = arr[n - 1] - arr[l]
            d1 = arr[r] - arr[0]
            cost = min(cost, abs(d2 - d1))
            if d1 < d2:
                l += 1
            else:
                r -= 1
        print(cost)


run_task()
def solve():
    n = int(input())
    for _ in range(n):
        m = int(input())
        arr = list(map(int, input().split()))
        arr.sort()
        new_arr = []
        l = 0
        r = len(arr) - 1
        while l < r:
            new_arr.append(arr[r])
            new_arr.append(arr[l])
            l += 1
            r -= 1
        if len(arr) % 2 != 0:
            new_arr.append(arr[l])
        cur_sum = new_arr[0]
        is_beauty = True
        for i in range(1, m):
            if cur_sum == new_arr[i]:
                is_beauty = False
                break
            cur_sum += new_arr[i]
        if is_beauty:
            print('YES')
            print(*new_arr)
        else:
            print('NO')


solve()
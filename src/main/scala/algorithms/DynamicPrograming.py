import math,functools

def domino(sum, n):
    dp = [0] * (n+1)
    dp[0] = 1
    dp[1] = 1
    for i in range(2, n+1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[-1]

#print(domino(0, 42) % 100)
#print(domino(0,100000) % 1000000000)

def domino3(n):
    dp = [0] * (n + 1)
    dp[0] = 1
    dp[1] = 1
    dp[2] = 1
    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 3]
    return dp[-1]

def print_path(p, i, j):
    if i == 0 and j == 0:
        return ''
    if p[i][j] == 0:
        path = print_path(p, i - 1, j)
        path += 'D'
    else:
        path = print_path(p, i, j - 1)
        path += 'R'
    return path

def find_bug_path(arr):
    dp = [[0] * len(arr[0]) for _ in range(len(arr))]
    p = [[0] * len(arr[0]) for _ in range(len(arr))]
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            dp[i][j] = arr[i][j]
            if i > 0 and dp[i - 1][j] + arr[i][j] > dp[i][j]:
                dp[i][j] = dp[i - 1][j] + arr[i][j]
                p[i][j] = 0
            if j > 0 and dp[i][j - 1] + arr[i][j] > dp[i][j]:
                dp[i][j] = dp[i][j - 1] + arr[i][j]
                p[i][j] = 1
    print(print_path(p, len(arr) - 1, len(arr[0]) - 1))
    return dp[-1][-1]

def input_find_bug(fn):
    with open(fn) as rd:
        r,c = map(int, rd.readline().split())
        arr = []
        for i in range(r):
            row = list(map(int, rd.readline().split()))
            arr.append(row)
        return find_bug_path(arr)

#print(input_find_bug('/Users/admin/Downloads/bug2.in'))



def find_rect_sum(arr,r,c):
    n = len(arr)
    m = len(arr[0])
    dp = [[0] * (m+1) for _ in range(n+1)]
    for i in range(n):
        #sum up by row
        for j in range(m):
            dp[i+1][j+1] = arr[i][j]
            dp[i+1][j+1] += dp[i + 1][j]
            dp[i+1][j+1] += dp[i][j + 1]
            dp[i+1][j+1] -= dp[i][j]
    return dp[r + 1][c + 1] - dp[r][c + 1] - dp[r + 1][c] + dp[r][c]

def input_rect_sum(fn):
    with open(fn) as rd:
        n,m = map(int,rd.readline().split())
        arr = []
        rect_sum = [[0] * (m + 1) for _ in range(n+1)]
        for i in range(n):
            row = list(map(int, rd.readline().split()))
            arr.append(row)
        for i in range(n):
            for j in range(m):
                rect_sum[i+1][j+1] = arr[i][j]
                rect_sum[i+1][j+1] += rect_sum[i][j+1]
                rect_sum[i+1][j+1] += rect_sum[i+1][j]
                rect_sum[i+1][j+1] -= rect_sum[i][j]
        q = int(rd.readline())
        total_sum = 0
        for i in range(q):
            x1,x2,y1,y2 = map(int, rd.readline().split())
            x1 -= 1
            x2 -= 1
            y1 -= 1
            y2 -= 1
            total_sum += rect_sum[x2+1][y2+1] - rect_sum[x1][y2+1] - rect_sum[x2+1][y1] + rect_sum[x1][y1]
        return total_sum

def input_rect_sum2():
    n,m = map(int,input().split())
    arr = []
    rect_sum = [[0] * (m + 1) for _ in range(n+1)]
    for i in range(n):
        row = list(map(int, input().split()))
        arr.append(row)
    for i in range(n):
        for j in range(m):
            rect_sum[i+1][j+1] = arr[i][j]
            rect_sum[i+1][j+1] += rect_sum[i][j+1]
            rect_sum[i+1][j+1] += rect_sum[i+1][j]
            rect_sum[i+1][j+1] -= rect_sum[i][j]
    q = int(input())
    total_sum = 0
    for i in range(q):
        x1,x2,y1,y2 = map(int, input().split())
        x1 -= 1
        x2 -= 1
        y1 -= 1
        y2 -= 1
        s = rect_sum[x2+1][y2+1] - rect_sum[x1][y2+1] - rect_sum[x2+1][y1] + rect_sum[x1][y1]
        total_sum += s
    return total_sum


#print(input_rect_sum('/Users/admin/Downloads/rectangle.in'))
#print(input_rect_sum2())

import math

def find_change(arr, s):
    dp = [0] * (s + 1)
    p = [0] * (s + 1)
    for i in range(1, s + 1):
        dp[i] = math.inf
        for j in range(len(arr)):
            if i - arr[j] >= 0 and dp[i-arr[j]] + 1 < dp[i]:
                dp[i] = dp[i-arr[j]] + 1
                p[i] = arr[j]
    #print_path_for_change(p, s)
    print
    return dp[s]


def print_path_for_change(p, i):
    if i == 0:
        return
    print_path_for_change(p, i - p[i])
    if i - p[i] > 0:
        print('+',end='')
    print(p[i],end='')

def input_find_change(fn):
    with open(fn) as rd:
        r,s = map(int, rd.readline().split())
        arr = list(map(int, rd.readline().split()))
        return find_change(arr, s)

#print(input_find_change('/Users/admin/Downloads/change.in'))

def backpack(c,w,W):
    n = len(c) + 1
    dp = [[0] * (W+1) for _ in range(n+1)]
    for i in range(1, n + 1):
        for j in range(W+1):
            dp[i][j] = dp[i-1][j]
            if j - w[i-1] >= 0:
                dp[i][j] = max(dp[i][j], dp[i-1][j-w[i-1]] + c[i-1])
    return dp[-1][-1]

def find_common_subsequence(s1, s2):
    n = len(s1)
    m = len(s2)
    dp = [[0] * (m+1) for _ in range(n+1)]
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])
            if s1[i-1] == s2[j - 1] and dp[i][j] < dp[i-1][j-1] + 1:
                dp[i][j] = dp[i-1][j-1] + 1
    print_common_subsequence(dp, s1, s2)
    return dp[-1][-1]

def print_common_subsequence(dp, s1, s2):
    res = []
    i = len(s1)
    j = len(s2)
    while i > 0 and j > 0:
        if s1[i-1] == s2[j-1]:
            res.append(str(s1[i-1]))
            i -= 1
            j -= 1
        elif dp[i-1][j] > dp[i][j-1]:
            i -= 1
        else:
            j -= 1
    print(''.join(res[::-1]))


def find_longest_increasing_subsequence(fn):
    with open(fn) as rd:
        n = int(rd.readline())
        arr = list(map(int, rd.readline().split()))
        dp = [1] * n
        for i in range(n):
            for j in range(i):
                if arr[i] > arr[j] and dp[i] < dp[j] + 1:
                    dp[i] = dp[j] + 1
        return max(dp)


def find_count_longest_increasing_subsequence(fn):
    with open(fn) as rd:
        n = int(rd.readline())
        arr = list(map(int, rd.readline().split()))
        qnt = 0
        max_len = 0
        #n = 5
        #arr = [7,1,3,2,4]
        dp = [1] * n
        c = [1] * n
        for i in range(n):
            for j in range(i):
                if arr[i] > arr[j] and dp[i] < dp[j] + 1:
                    dp[i] = dp[j] + 1
                    c[i] = c[j]
                elif arr[i] > arr[j] and dp[i] == dp[j] + 1:
                    c[i] += c[j]
            if dp[i] > max_len:
                max_len = dp[i]
                qnt = c[i]
            elif dp[i] == max_len:
                qnt += c[i]
        return (max_len, qnt)


#print(find_count_longest_increasing_subsequence('/Users/admin/Downloads/lis.in'))
#print(find_common_subsequence([1,2,3,4],[3,1,4,5,3,1,2,4]))


#find_change([1,2,3,4,5],10)
#arr = [[1, 4, 1, 2, 3], [2, 3, 2, 1, 4], [1, 1, 1, 2, 4], [2, 5, 1, 7, 1]]
#arr = [[1,1,1],[1,1,1]]
#print(find_rect_sum(arr, 0, 0))
# print(domino3(10))

def bynomical_coeff(n, k):
    dp = [[0] * (k + 1) for _ in range(n+1)]
    for i in range(len(dp)):
        dp[i][0] = 1
    for i in range(len(dp[0])):
        dp[i][i] = 1
    for i in range(1,n+1):
        for j in range(1,k+1):
            dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
    return dp[-1][-1]


def find_backback(n,W,cost,weight):
    dp = [[0] * (1 + W) for _ in range(n+1)]
    ps = []
    for i in range(1, n+1):
        for j in range(W+1):
            dp[i][j] = dp[i-1][j]
            if j - weight[i-1] >= 0 and dp[i-1][j-weight[i-1]] + cost[i-1] > dp[i][j]:
                dp[i][j] = dp[i-1][j-weight[i-1]] + cost[i-1]
    w = W
    profit = dp[-1][-1]
    things = []
    for i in range(n,0,-1):
        if profit < 0:
            break
        if profit == dp[i-1][w]:
            continue
        things.append(i)
        w -= weight[i-1]
        profit -= cost[i-1]
    print(*things[::-1])
    return dp[-1][-1]

def input_find_backpack():
    n,W = map(int, input().split())
    weight = [0] * n
    cost = [0] * n
    for i in range(n):
        w,c = map(int, input().split())
        weight[i] = w
        cost[i] = c
    return find_backback(n, W, cost, weight)

def input_find_backpac2(fn):
    with open(fn) as rd:
        n,W = map(int, rd.readline().split())
        weight = [0] * n
        cost = [0] * n
        for i in range(n):
            w,c = map(int, rd.readline().split())
            weight[i] = w
            cost[i] = c
    return find_backback(n, W, cost, weight)


def find_com_log_seq(s1,s2):
    n = len(s1)
    m = len(s2)
    dp = [[0] * (m+1) for _ in range(n+1)]
    for i in range(1,n+1):
        for j in range(1, m + 1):
            dp[i][j] = max(dp[i][j-1],dp[i-1][j])
            if s1[i-1]==s2[j-1]:
                dp[i][j] = max(dp[i][j],dp[i-1][j-1] + 1)
    res = []
    i = n
    j = n
    while i > 0 and j > 0:
        if s1[i-1] == s2[j-1]:
            res.append(str(s1[i-1]))
            i -= 1
            j -= 1
        elif dp[i][j-1] > dp[i-1][j]:
            j -= 1
        else:
            i -= 1
    print(' '.join(res[::-1]))
    return dp[-1][-1]

def input_find_com_log_seq():
    n = int(input())
    s1 = list(map(int, input().split()))
    m = int(input())
    s2 = list(map(int, input().split()))
    return find_com_log_seq(s1,s2)


def input_find_com_log_seq2(fn):
    with open(fn) as rd:
        n = int(rd.readline())
        s1 = list(map(int, rd.readline().split()))
        m = int(rd.readline())
        s2 = list(map(int, rd.readline().split()))
        return find_com_log_seq(s1,s2)

#print(input_find_com_log_seq())
#print(input_find_com_log_seq2('/Users/admin/Downloads/seq2.in'))

#print(input_find_backpac2('/Users/admin/Downloads/rucksack.in'))
#print(input_find_backpack())

def find_arithm(arr,i, x ,cur_path,need_sum):
    if i == len(arr):
        if x == need_sum:
            return cur_path
        return []
    if i == 0:
        return find_arithm(arr,i+1,arr[i],cur_path + [str(arr[i])],need_sum) or find_arithm(arr,i+1,arr[i],cur_path + [str(arr[i])],need_sum)
    else:
        return find_arithm(arr, i + 1, x-arr[i], cur_path + ['-',str(arr[i])], need_sum) or find_arithm(arr, i + 1, x+arr[i],
                                                                                                  cur_path + ['+',
                                                                                                      str(arr[i])],
                                                                                                  need_sum)

def input_find_arithm():
    n,need_sum = map(int, input().split())
    arr = list(map(int, input().split()))
    return find_arithm(arr,0,arr[0],[],need_sum)

def input_find_arithm2(fn):
    with open(fn) as rd:
        n,need_sum = map(int, rd.readline().split())
        arr = list(map(int, rd.readline().split()))
        return find_arithm(arr,0,arr[0],[],need_sum)


print(''.join(input_find_arithm2('/Users/admin/Downloads/arithm2.in')))

#print(''.join(input_find_arithm()))



#print(bynomical_coeff(3,2))#3
#print(bynomical_coeff(50,20))
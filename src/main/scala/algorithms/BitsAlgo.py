def a_23_26():
    return 23 ^ 26

def count_butterfly(n):
    return (1 << n)-1

def count_sum(arr):
    pre = [0] * len(arr)
    n = len(arr)
    for mask in range(1 << n):
        for j in range(n):
            if mask & (1 << j):
                pre[mask] = pre[mask ^ (1 << j)] + arr[j]
                break
    return pre


import math

def salesman2(arr):
    n = len(arr)
    dp = [[math.inf] * n for _ in range(1 << n)]
    dp[0][0] = 0
    for mask in range(1 << n):
        for i in range(n):
            # he doesn't visit i city, skip it.
            if dp[mask][i] == math.inf:
                continue
            for j in range(n):
                #where he can go from i to other city.
                if (mask & (1 << j)) == 0:
                    dp[mask | (1 << j)][j] = min(dp[mask | 1 << j][j], dp[mask][i] + arr[i][j])
    return dp



def can_go(mask,new_mask, mistmach):
    # 0 in mask matches 1 in new_mask
    if mask & new_mask != 0:
        return False
    or_mask = mask | new_mask
    if or_mask in mistmach:
        return False
    return True

from collections import defaultdict
def pre_calc_mistmatch(n):
    mismatch = set()
    for mask in range(1 << n):
        cnt = 0
        for i in range(n):
            if mask & (1 << i) != 0:
                if cnt > 0 and cnt %2 != 0:
                    mismatch.add(mask)
                    break
                cnt = 0
            else:
                cnt += 1
        if cnt > 0 and cnt % 2 != 0:
            mismatch.add(mask)
    return mismatch


def parquet(n,m, k):
    # m > n
    n1 = min(n,m)
    m1 = max(n,m)
    m = m1
    n = n1
    # m is column number
    mismatch = pre_calc_mistmatch(n)
    dp = [[0] * (1 << n) for _ in range(m+1)]
    dp[0][0] = 1
    mask_to_mask= defaultdict(list)
    for mask in range(1 << n):
        for new_mask in range(1 << n):
            #print(new_mask)
            if mask & new_mask != 0 or (mask | new_mask) in mismatch:
                continue
            mask_to_mask[mask].append(new_mask)

    for i in range(m):
        for mask in mask_to_mask:
            for new_mask in mask_to_mask[mask]:
                dp[i + 1][new_mask] = (dp[i + 1][new_mask] % k + dp[i][mask] % k) % k
        # for mask in range(a):
        #     for new_mask in range(a):
        #         if mask & new_mask != 0 or  (mask | new_mask) in mismatch:
        #             continue
        #         dp[i+1][new_mask] = (dp[i+1][new_mask] % k + dp[i][mask] % k) % k
    return dp[m][0]


def show_comb(n, need_i):
    res = []
    i = 1
    for mask in range(1 << n):
        comb = []
        for j in range(n):
            if (1 << j) & mask:
                comb.append(j + 1)
        comb = ','.join(list(map(str, comb)))
        res.append('{'+comb + '}')
    res.sort()
    print(res[need_i-1])



#show_comb(9, 365)

#print(parquet(3,2,10))#3
#print(parquet(5,6,1000000000))#1183
#print(parquet(5000,6,1000000000))#938355277
#print(parquet(16,16,1000000000))
#print(count_butterfly(5))

####################### Test
def count_one_bits_from_file(fn):
    with open(fn) as rd:
        n = int(rd.readline())
        nums = list(map(int, rd.readline().split()))
        count_one_bits(n, nums)

def count_one_bits(n, nums):
    bits_cnt = [0] * n
    for i in range(n):
        cnt = 0
        num = nums[i]
        while num:
            if (num & 1) != 0:
                cnt += 1
            num >>= 1
        bits_cnt[i] = cnt
    print(*bits_cnt)

def count_one_bits_from_con():
    n = int(input())
    nums = list(map(int, input().split()))
    count_one_bits(n, nums)

#count_one_bits_from_file('/Users/admin/Downloads/ones.in')



def salesman(arr, p):
    n = len(arr)
    dp = [[math.inf] * n for _ in range(1 << n)]
    dp[0][0] = 0
    for mask in range(1 << n):
        for i in range(n):
            if dp[mask][i] == math.inf:
                continue
            for j in range(n):
                if (mask & (1 << j)) == 0:
                    if dp[mask ^ (1 << j)][j] > dp[mask][i] + arr[i][j]:
                        dp[mask ^ (1 << j)][j] = dp[mask][i] + arr[i][j]
                        p[mask ^ (1 << j)][j] = i
    return dp

def find_path(arr, dp, p):
    n = len(arr)
    cur_path = [0]
    cur_len = dp[(1<<n) - 1][0]
    last_city = p[(1 << n) - 1][0]
    cur_len -= arr[last_city][0]
    cur_path.append(last_city)
    seen = set()
    while cur_len > 0:
        for mask in range((1 << n) - 2,-1,-1):
            #check if mask doesn't contain visited cities
            contains = False
            for c in seen:
                if (1 << c) & mask != 0:
                    contains = True
                    break
            if contains:
                continue
            if (1 << last_city) & mask != 0 and cur_len == dp[mask][last_city]:
                seen.add(last_city)
                new_last_city = p[mask][last_city]
                cur_len -= arr[new_last_city][last_city]
                cur_path.append(new_last_city)
                last_city = new_last_city
                break
    return cur_path

def salesman_from_file(fn):
    with open(fn) as rd:
        n = int(rd.readline())
        arr = []
        for _ in range(n):
            row = list(map(int, rd.readline().split()))
            arr.append(row)
        p = [[0] * n for _ in range(1 << n)]
        dp = salesman(arr, p)
        cur_path = find_path(arr, dp, p)
        check_path(arr, cur_path, dp[(1 << n) - 1][0])
        print(dp[(1 << n) - 1][0])
        print(*cur_path)
def salesman_from_con():
    n = int(input())
    arr = []
    for _ in range(n):
        row = list(map(int, input().split()))
        arr.append(row)
    p = [[0] * n for _ in range(1 << n)]
    dp = salesman(arr, p)
    cur_path = find_path(arr,dp,p)
    check_path(arr,cur_path,dp[(1<<n) - 1][0])
    print(dp[(1 << n) - 1][0])
    print(*cur_path)

def check_path(arr,p,need_len):
    cur_len = 0
    i = 1
    while i < len(p):
        cur_len += arr[p[i-1]][p[i]]
        i += 1
    cur_len += arr[p[-1]][0]
    assert cur_len == need_len, 'checked'


def input_friends_from_con():
    n,m = map(int, input().split())
    #n is person number
    friends = [0] * n
    for _ in range(m):
        a,b = map(int, input().split())
        a -= 1
        b -= 1
        friends[a] |= 1 << b
        friends[b] |= 1 << a
    for i in range(n):
        friends[i] |= 1 << i
    max_grp_cnt = 0
    for mask in range(1 << n):
        flg = True
        grp = 0
        for i in range(n):
            if (1 << i) & mask != 0:
                grp += 1
                if mask & friends[i] != mask:
                    flg = False
                    break
        if flg:
            max_grp_cnt = max(max_grp_cnt, grp)

    print(max_grp_cnt)

def input_friends_from_file(fn):
    with open(fn) as rd:
        n,m = map(int, rd.readline().split())
        friends = [0] * n
        for _ in range(m):
            a,b = map(int, rd.readline().split())
            a -= 1
            b -= 1
            friends[a] |= 1 << b
            friends[b] |= 1 << a
    for i in range(n):
        friends[i] |= 1 << i
    max_grp_cnt = 0
    for mask in range(1 << n):
        flg = True
        grp = 0
        for i in range(n):
            if (1 << i) & mask != 0:
                grp += 1
                if mask & friends[i] != mask:
                    flg = False
                    break
        if flg:
            max_grp_cnt = max(max_grp_cnt, grp)
    print(max_grp_cnt)


def find_min_news_grp():
    n,m = map(int, input().split())
    f = [0] * n
    for _ in range(m):
        a,b = map(int, input().split())
        a -= 1
        b -= 1
        f[a] |= 1 << b
        f[b] |= 1 << a
    for i in range(n):
        f[i] |= 1 << i
    min_grp_cnt = math.inf
    for mask in range(1 << n):
        #check if mask is min group
        grp_cnt = 0
        flg = True
        grp_mask = 0
        for i in range(n):
            if (1 << i) & mask != 0:
                grp_cnt += 1
                grp_mask |= f[i]
                if f[i] & mask != mask:
                    flg = False
                    break
        if flg and grp_mask == (1 << n) - 1:
            min_grp_cnt = min(min_grp_cnt, grp_cnt)
    print(min_grp_cnt)

def find_min_news_grp_from_file(fn):
    with open(fn) as rd:
        n, m = map(int, rd.readline().split())
        f = [0] * n
        for _ in range(m):
            a, b = map(int, rd.readline().split())
            a -= 1
            b -= 1
            f[a] |= 1 << b
            f[b] |= 1 << a
        for i in range(n):
            f[i] |= 1 << i
        min_grp_cnt = math.inf
        for mask in range(1 << n):
            # check if mask is min group
            grp_cnt = 0
            grp_mask = 0
            for i in range(n):
                #check people that will be notified
                if (1 << i) & mask != 0:
                    grp_cnt += 1
                    grp_mask |= f[i]
            #check if notify all people
            if grp_mask == (1 << n) - 1:
                min_grp_cnt = min(min_grp_cnt, grp_cnt)
        print(min_grp_cnt)


#input_friends_from_file('/Users/admin/Downloads/friends2.in')

#input_friends_from_con()
#find_min_news_grp_from_file('/Users/admin/Downloads/new.in')
find_min_news_grp_from_file('/Users/admin/Downloads/new2.in')


#salesman_from_con()
#salesman_from_file('/Users/admin/Downloads/salesman2.in')




import math
import bisect
def gen_all_words(template,idx, temp_pos,pos,need_pos):
    if idx == len(temp_pos):
        pos[0] += 1
        if pos[0] == need_pos:
            print(''.join(template))
        return
    for ch in 'abcde':
        template[temp_pos[idx]] = ch
        gen_all_words(template,idx + 1,temp_pos,pos,need_pos)


def gen_all_words_from_con():
    temp = list(input().strip())
    temp_pos = []
    for i in range(len(temp)):
        if temp[i] == '?':
            temp_pos.append(i)
    if len(temp_pos) == 0:
        print(''.join(temp))
    else:
        pos = [0]
        gen_all_words(temp, 0, temp_pos,pos,5151)

def find_warehouse_for_shop(warehouses, shops):
    warehouses.sort()
    shops.sort()
    i = 0
    j = 0
    total_dist = 0
    while i < len(warehouses) and j < len(shops):
        total_dist += abs(warehouses[i] - shops[j])
        i += 1
        j += 1
    print(total_dist)


def find_warehouse_for_shop_for_con():
    n = int(input())
    shops = list(map(int, input().split()))
    warehouses = list(map(int, input().split()))
    find_warehouse_for_shop(warehouses, shops)

def find_warehouse_for_shop_from_file(fn):
    with open(fn) as rd:
        n = int(rd.readline())
        shops = list(map(int, rd.readline().split()))
        warehouses = list(map(int, rd.readline().split()))
        find_warehouse_for_shop(warehouses, shops)

from functools import lru_cache

def golden_bar(arr):
    total_sum = sum(arr)

    def find_sum(total_sum, n):
        min_diff = math.inf
        for mask in range(1 << n):
            cur_sum = 0
            for i in range(n):
                if mask & (1 << i) != 0:
                    cur_sum += arr[i]
                if cur_sum > total_sum:
                    break
            min_diff = min(min_diff, abs(total_sum - 2 * cur_sum))
        return min_diff

    n = len(arr)
    print(find_sum(total_sum, n))

def golden_bar_from_con():
    int(input())
    arr = list(map(int, input().split()))
    golden_bar(arr)

golden_bar_from_con()

def golden_bar_from_file(fn):
    with open(fn) as rd:
        n = int(rd.readline())
        arr = list(map(int, rd.readline().split()))
        golden_bar(arr)

#golden_bar_from_con()

def dishonest_golden_bar(arr):
    arr.sort()
    half = len(arr) // 2
    s1 = 0
    s = sum(arr)
    for i in range(half):
        s1 += arr[i]
    print(abs(s - 2*s1))

def dishonest_golden_bar_from_con():
    int(input())
    arr = list(map(int, input().split()))
    dishonest_golden_bar(arr)

def dishonest_golden_bar_from_con(fn):
    with open(fn) as rd:
        n = int(rd.readline())
        arr = list(map(int, rd.readline().split()))
        dishonest_golden_bar(arr)



#dishonest_golden_bar_from_con('/Users/admin/Downloads/gold4.in')

def time_managment(arr):
    # 0 is time,1 is deadline
    n = len(arr)
    dp = [[0] * 20008 for _ in range(n+1)]
    for i in range(n):
        for t in range(20008):
            #case when we don't do job i + 1
            dp[i+1][t] = max(dp[i+1][t],dp[i][t])
            if t > arr[i][1]:
                #can't do the job i
                continue
            dp[i+1][t+arr[i][0]] = max(dp[i+1][t+arr[i][0]],dp[i][t] + 1)
    print(max(dp[-1]))


    # @lru_cache(None)
    # def do_job(idx,cur_time):
    #     if idx == len(arr):
    #         return 0
    #     max_cnt = 0
    #     if cur_time <= arr[idx][1]:
    #         max_cnt = 1 + do_job(idx +1, cur_time + arr[idx][0])
    #     return max(max_cnt, do_job(idx + 1,cur_time))
    #
    # print(do_job(0, 0))


def test_time_managment(arr):
    #0 is time,1 is deadline
    n = len(arr)
    max_cnt = 0
    for mask in range(1 << n):
        cur_time = 0
        cnt = 0
        for i in range(n):
            if mask & (1 << i) != 0:
                if cur_time <= arr[i][1]:
                    cnt += 1
                    cur_time += arr[i][0]
                else:
                    cnt = 0
                    break
        max_cnt = max(cnt, max_cnt)
    return max_cnt




def time_managment_from_con():
    n = int(input())
    arr = [0] * n
    for i in range(n):
        t,d = list(map(int, input().split()))
        arr[i] = [t,d]
    #print(test_time_managment(arr))
    time_managment(arr)



def time_managment_from_file(fn):
    with open(fn) as rd:
        n = int(rd.readline())
        arr = [0] * n
        for i in range(n):
            t,d = list(map(int, rd.readline().split()))
            arr[i] = [t,d]
        #print(test_time_managment(arr))
        time_managment(arr)


#time_managment_from_file('/Users/admin/Downloads/time2.in')

#time_managment_from_con()


golden_bar_from_file('/Users/admin/Downloads/gold3.in')

#find_warehouse_for_shop_from_file('/Users/admin/Downloads/shops2.in')
#find_warehouse_for_shop_for_con()


#gen_all_words_from_con()





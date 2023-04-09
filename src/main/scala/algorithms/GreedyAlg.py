def change(coins, s):
    cnt = 0
    for coin in coins:
        cnt += s // coin
        s %= coin
    return cnt

 #1, 2, 8 и 10 можно набрать сумму 27
#print(change([10,8,2,1], 27))

def calc_schedule():
    n = int(input())
    deadline = []
    for i in range(n):
        d,c = input().split()
        deadline.append([int(d),int(c)])
    deadline.sort(key=lambda x:-x[1])
    max_day = max(deadline,key=lambda x:x[0])
    used = [False] * (max_day[0] + 1)
    total_cost = 0
    for d,c in deadline:
        j = d
        while j > 0 and used[j]:
            j -= 1
        if j == 0:
            continue
        used[j] = True
        total_cost += c
    return total_cost


#print(calc_schedule())


def schedule(deadline,cost,index):
    used = set()
    cur_sum = 0
    for j in range(len(index)):
        i = index[j]
        k = deadline[i]
        while k >= 1 and used[k]:
            k -= 1
        if k == 0:
            continue
        used[k] = True
        cur_sum += cost[i]
    return cur_sum

# deadline = [1, 2, 2, 3, 5]
# cost = [2, 5, 4, 1, 3]
# index = [i for i in range(len(cost))]
# index.sort(key=lambda x:cost[x],reverse=True)
# used = [False] * (max(deadline)+1)
# print(schedule(deadline, cost,index, used))

def pick_tasks(app):
    cnt = 1
    last = 0
    for i in range(1,len(app)):
        if app[i][0] >= app[last][1]:
            cnt += 1
            last = i
    return cnt

def calc_tasks(fn):
    with open(fn) as rd:
        n = int(rd.readline())
        task = []
        for _ in range(n):
            s,e = map(int, rd.readline().split())
            task.append([s, e])
        task.sort(key=lambda x:x[1])
        return pick_tasks(task)

#print(calc_tasks('/Users/admin/Downloads/request2.in'))

def calc_dist(gas,dist,tank):
    cur_dist = 0
    cnt = 0
    while cur_dist < dist:
        if cur_dist + tank >= dist:
            break
        # need to fill the tank
        k = cur_dist + tank
        while k > 0 and not gas[k]:
            k -= 1
        cur_dist = k
        cnt += 1
    return cnt

#print(calc_dist([0,0,0,3,4,0,6,0,0,0,0],10,4))


def fill_tank(fn):
    with open(fn) as rd:
        n,dist,tank = map(int, rd.readline().split())
        gas = [False] * (dist + 1)
        gas_dist = map(int, rd.readline().split())
        for d in gas_dist:
            gas[d] = True
        return calc_dist(gas,dist,tank)

#print(fill_tank('/Users/admin/Downloads/petrol2.in'))


def backpack(cost, weight, W):
    cost_for_kg = [(cost[i]/weight[i],i) for i in range(len(cost))]
    cost_for_kg.sort(key=lambda x:-x[0])
    total_cost = 0
    for i in range(len(cost_for_kg)):
        (c, j) = cost_for_kg[i]
        if W - weight[j] >= 0:
            total_cost += cost[j]
            W -= weight[j]
        else:
            break
    return total_cost

def input_backpack_idefinite(fn):
    with open(fn) as rd:
        n,W = map(int, rd.readline().split())
        cost = []
        weight = []
        for _ in range(n):
            w,c = map(int, rd.readline().split())
            cost.append(c)
            weight.append(w)
        return backpack_idefinite(cost,weight,W)


def backpack_idefinite(cost, weight, W):
    cost_for_kg = [(cost[i]/weight[i],i) for i in range(len(cost))]
    cost_for_kg.sort(key=lambda x:-x[0])
    total_cost = 0
    for i in range(len(cost_for_kg)):
        (c, j) = cost_for_kg[i]
        if W - weight[j] >= 0:
            total_cost += cost[j]
            W -= weight[j]
        else:
            total_cost += int(W / weight[j] * cost[j])
            break
    return total_cost


#print(input_backpack_idefinite('/Users/admin/Downloads/cont2.in'))
import math

def count_lecture_hall(task):
    #task.sort(key=lambda x:x[1])
    event = []
    for a,b in task:
        event.append((a,1))
        event.append((b,-1))
    event.sort()
    cnt = 0
    max_cnt = 0
    for a,tp in event:
        if tp == 1:
            cnt += 1
        else:
            cnt -= 1
        max_cnt = max(max_cnt, cnt)
    return max_cnt


def input_count_lecture_hall2():
    n = int(input())
    task = []
    for _ in range(n):
        l, r = map(int, input().split())
        task.append([l,r])
    return count_lecture_hall(task)



def input_count_lecture_hall(fn):
    with open(fn) as rd:
        n = int(rd.readline())
        task = []
        for _ in range(n):
            l,r = map(int, rd.readline().split())
            task.append([l,r])
    return count_lecture_hall(task)

#print(input_count_lecture_hall2())
#print(input_count_lecture_hall('/Users/admin/Downloads/request2.in'))


def calc_olymiad(totat_time, times):
    times.sort()
    fine_time = 0
    task_cnt = 0
    cur_time = 0
    for t in times:
        if cur_time + t >= totat_time:
            break
        fine_time += cur_time + t
        cur_time += t
        task_cnt += 1
    return [task_cnt, fine_time]

def input_calc_olymiad():
    n,total_time = map(int, input().split())
    times = list(map(int, input().split()))
    return ' '.join(map(str, calc_olymiad(total_time, times)))

def input_calc_olymiad2(fn):
    with open(fn) as rd:
        n,total_time = map(int, rd.readline().split())
        times = list(map(int, rd.readline().split()))
        return ' '.join(map(str, calc_olymiad(total_time, times)))

#print(input_calc_olymiad2('/Users/admin/Downloads/contest.in'))

from collections import Counter

def input_calc_ice():
    n = int(input())
    freq = Counter()
    for _ in range(n):
        s = input()
        freq[s] += 1
    return max(freq.values())

def input_calc_ice2(fn):
    with open(fn) as rd:
        n = int(rd.readline())
        prod_cnt = 1
        uniq_sort = set()
        for _ in range(n):
            s = rd.readline()
            if s in uniq_sort:
                prod_cnt += 1
                uniq_sort = set()
                uniq_sort.add(s)
            else:
                uniq_sort.add(s)
        return prod_cnt


#print(input_calc_ice2('/Users/admin/Downloads/ice.in'))
print(input_calc_ice2('/Users/admin/Downloads/ice2.in'))

def input_lecture_hall(fn):
    with open(fn) as rd:
        n = int(rd.readline())
        task = []
        for _ in range(n):
            s,e = map(int, rd.readline().split())
            task.append([s,e])


#c = [10, 12], w = [2, 3], W = 4.
#print(backpack([10,12], [2, 3], W = 4))
#print(backpack([12, 15, 18], [3, 3, 9], W = 10))#9
#print(backpack([10, 20, 30], [2, 5, 10], W = 12))#9
#print(backpack([10, 20, 30], [2, 5, 10], W = 10))#9
#[10, 20, 30], w = [2, 5, 10], W = 12.
#c = [10, 20, 30], w = [2, 5, 10], W = 10
#print(backpack([10,20,30],[2, 5, 10],10))#9
#c = [10, 12], w = [2, 3], W = 4
#print(backpack([10,12],[2,3],4))
#print(backpack_idefinite([10, 20, 30], [2, 5, 10],12))#
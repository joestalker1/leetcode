def permutation(arr, idx, m):
    if idx == len(arr):
        return
    for i in range(1, m + 1):
        arr[idx] = i
        permutation(arr, idx + 1)


def permutation_without_rep(arr,used, idx, m):
    if len(arr) == idx:
        return
    for i in range(1, m + 1):
        if i in used:
            continue
        used.add(i)
        arr[idx] = i
        permutation_without_rep(arr, used, idx+1, m)
        used.discard(i)

def generate_bracket(arr,idx, bal):
    if idx == len(arr):
        return
    arr[idx] = '('
    generate_bracket(arr,idx +1,bal + 1)
    if bal == 0:
        return
    arr[idx] = ')'
    generate_bracket(arr,idx+1,bal - 1)

def generate_term(arr,idx,sum,last, n):
    if idx == len(arr):
        return
    for i in range(last,n - sum + 1):
        arr[idx] = i
        generate_bracket(arr,idx + 1,sum+i,i,n)

import math
ans = math.inf


class Salesman:
    def __init__(self, arr):
        self.min_path = math.inf
        self.path = []
        self.arr = arr

    def calc(self):
       n = len(self.arr)
       def find_path(arr,idx, cur_len, p,used):
           if cur_len >= self.min_path:
               return
           if idx == n:
               cur_len += arr[p[idx-1]][0]
               if cur_len < self.min_path:
                   self.min_path = cur_len
                   self.path = p
               return
           for i in range(1, n):
               if used[i]:
                   continue
               used[i] = 1
               find_path(arr,idx+1,cur_len + arr[p[idx-1]][i],p + [i],used)
               used[i] = 0

       used = [0] * n
       find_path(self.arr,1,0, [0], used)

def salesman_from_con():
    n = int(input())
    arr = []
    for _ in range(n):
        row = list(map(int, input().split()))
        arr.append(row)
    salesman = Salesman(arr)
    salesman.calc()
    return [salesman.min_path,salesman.path]


#print(salesman_from_con())
def salesman_from_file(fn):
    with open(fn) as rd:
        n = int(rd.readline())
        arr = []
        for _ in range(n):
            row = list(map(int, rd.readline().split()))
            arr.append(row)
        salesman = Salesman(arr)
        salesman.calc()
        check_path(salesman.arr,salesman.path,salesman.min_path)
        return [salesman.min_path, salesman.path]


def check_path(arr,p,need_len):
    cur_len = 0
    i = 1
    while i < len(p):
        cur_len += arr[p[i-1]][p[i]]
        i += 1
    cur_len += arr[p[-1]][0]
    assert cur_len == need_len, 'checked'

_, p = salesman_from_file('/Users/admin/Downloads/salesman2.in')
print(*p)
        


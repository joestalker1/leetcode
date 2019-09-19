s = raw_input(' ')
n,x,y=s.split(' ')
n=int(n)
x=int(x)
y=int(y)
contests = []
v = []
w = []
for i in range(n):
    s = raw_input(' ')
    arr = s.split(' ')
    contests.append(map(lambda a:int(a), arr))

s = raw_input(' ')
v = [int(x) for x in s.split(' ')]
v.sort()

s = raw_input(' ')
w = [int(x) for x in s.split(' ')]
w.sort()

min_time = float('inf')

def find_val(arr, target):
    s = 0
    e = len(arr) - 1
    while s <= e:
        mid = s + (e - s) // 2
        if arr[mid] > target:
            e = mid - 1
        elif arr[mid] < target:
            s = mid + 1
        else:
            return mid
    if s > e:
        return e
    return s

for t1,t2 in contests:
    i = find_val(v, t1)
    if i == len(v) or i == -1 or v[i] > t1:
        continue
    closest_v = v[i]
    i = find_val(w, t2)
    if i == len(w) or i == -1 or w[i] > t2:
        continue
    closest_w = w[i]
    min_time = min(min_time, closest_w - closest_v + 1)

print(min_time)







from bisect import bisect_left,bisect_right

s = input(' ')
n,x,y=s.split(' ')
n=int(n)
x=int(x)
y=int(y)

contests = []

for i in range(n):
    s = input(' ')
    arr = s.split(' ')
    contests.append([int(arr[0]), int(arr[1])])

#enter to portals
s = input(' ')
v = []
for a in s.split(' '):
    v.append(int(a))
v.sort()

w = []
#exit from portals
s = input(' ')
for a in s.split(' '):
    w.append(int(a))
w.sort()

contests.sort()
j1 = 0
min_item = float('inf')
for i in range(len(contests)):
    s,e = contests[i]
    j1 = bisect_right(v, s)
    a = float('-inf')
    if 0 <= j1-1 < len(v):
        a = v[j1-1]

    j2 = bisect_left(w, e)
    b = float('inf')
    if 0 <= j2 < len(w):
        b = w[j2]

    min_item = min(min_item, b - a + 1)
print(min_item)









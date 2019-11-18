n = int(input())
a = [0] * n
d = [0] * n

for i in range(n):
    s = input(' ')
    arr = s.split()
    a[i] = int(arr[0])
    d[i] = int(arr[1]) + int(arr[2])

indices = [i for i in range(n)]
indices.sort(key=lambda i: d[i],reverse=True)

i = indices[0]
max_val = a[i] + d[i]
acc = a[i] # delay
for j in range(1, len(indices)):
    i = indices[j]
    max_val = max(max_val, a[i] + d[i] + acc)
    acc += a[i]

print(max_val)









n = int(input())
s = input()
s = s.split()

a = [int(a) for a in s]

s = input()
s = s.split()

b = [int(b) for b in s]

def range_sum(a,b, i, j):
    if i == j:
        return a[i]
    s = a[i] + a[j]
    if i < j:
        for k in range(i+1, j):
            s += b[k]
        return s
    else:
        for k in range(1, j):
            s += b[k]
        for k in range(i + 1, n):
            s += b[k]
        return s


max_sum = 0

for i in range(n):
    for j in range(n):
        max_sum = max(max_sum, range_sum(a, b, i, j))
        if j > i:
            max_sum = max(max_sum, range_sum(a, b, j, i))
print(max_sum)





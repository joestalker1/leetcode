n = int(input())
s = input()

s = s.split()
a = []
for i in range(len(s)):
    a.append(int(s[i]))

s = input()
s = s.split()
b = []
for i in range(len(s)):
    b.append(int(s[i]))

pref = [b[0]]
for i in range(1, len(b)):
    pref.append(pref[i - 1] + b[i])

diff = [a[0] - pref[0]]
for i in range(1, len(b)):
    diff.append(max(diff[i - 1], a[i] - pref[i]))

max_sum = max(a)#i == j
#i < j
for i in range(1, n):
    max_sum = max(max_sum, a[i] + pref[i - 1] + diff[i - 1])

sum1 = [a[0]]
for i in range(1, len(b)):
    sum1.append(max(sum1[i-1], a[i] + pref[i-1]))
# i > j
for i in range(1, len(b)):
    max_sum = max(max_sum, a[i] + pref[n-1] - pref[i] + sum1[i-1])
print(max_sum)

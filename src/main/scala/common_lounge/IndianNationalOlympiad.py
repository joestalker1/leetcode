n = int(input())
s = input()
s = s.split()

a = [0]
for i in range(len(s)):
    a.append(int(s[i]))

s = input()
s = s.split()
b = [0]
for i in range(len(s)):
    b.append(int(s[i]))

max_sum = 0
pref = [0]
for i in range(1, len(b)):
    pref.append(pref[-1] + b[i])

diff = [float('-inf')]
for i in range(1, len(b)):
    diff.append(max(diff[i - 1], a[i] - pref[i]))

max_sum = max(a)
for j in range(2, n + 1):
    max_sum = max(max_sum, a[j] + pref[j - 1] + diff[j - 1])

diff = [a[n-1] - pref[n-1]]
for i in range(len(b) - 2, 0, -1):
    diff.insert(0, max(diff[0], a[i] - pref[i]))

diff.insert(0, float('-inf'))

for j in range(1, n):
    # i > j
    max_sum = max(max_sum, a[j] + pref[n] + diff[j+1] + pref[j - 1])

# for i in range(1, n + 1):
#     for j in range(1, n + 1):
#         if i == j:
#             max_sum = max(max_sum, a[i])
#         elif i < j:
#             max_sum = max(max_sum, a[i] + a[j] + pref[j - 1] - pref[i])
#         else:
#             # i > j
#             max_sum = max(max_sum, a[j] + pref[n] + (a[i] - pref[i]) + pref[j - 1])
print(max_sum)

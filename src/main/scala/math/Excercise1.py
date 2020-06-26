n = input()

n = int(n)
if n < 2:
    print(0)
    exit(0)
isPrime = [1] * (n + 1)
isPrime[0] = 0
isPrime[1] = 0

i = 2
while i * i <= n:
    if isPrime[i] == 1:
        j = i * i
        while j <= n:
            isPrime[j] = 0
            j += i
    i += 1
count = 0
for i in range(1, n + 1):
    if isPrime[i] == 1:
        count += 1
print(count)

def countPerfectNumber(n):
    count = 0
    for a in range(1, n + 1):
        if a ** (1. / 3) == a ** (1. / 2):
            count += 1
    return count

def countMultipeOf2And5(n):
    count = 0
    for a in range(1,n+1):
        if a % 2 == 0 and a % 5 == 0:
            count += 1
    return count

def countMultipeOf12(n):
    count = 0
    for a in range(1,n+1):
        if a ** 12 <= n:
            count += 1
        else:
            break
    return count
print(10**6 - 3)
print(countMultipeOf12(10**6))

print(countMultipeOf2And5(1000))
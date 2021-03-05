def gornerSchema(a, x):
    n = len(a) - 1
    k = 0
    y = a[n]
    while k != n:
        k += 1
        y = y * x + a[n - k]
    return y

def subseq_of(x,y):
    n1 = len(x)
    k1 = len(y)
    while n1 > 0 and k1 > 0:
        if x[n1] == y[k1]:
            n1 -= 1
            k1 -= 1
        else:
            n1 -= 1
        n1 -= 1
    return k1 == 0

def max_len_of_increasing_subseq(x):
    u = [0] * (2*len(x))
    n1 = 0
    k = 0
    u[0] = x[0]
    n = len(x)
    while n1 != n:
        n1 += 1
        i = 0
        j = k + 1
        while (j-i) != 1:
            s = i + (j-i) // 2
            if x[n1] <= u[s]:
                j = s
            else:
                i = s
        #{u[i] < x[n1] <= u[j], j - i = 1}
        if i == k:
            k += 1
            u[k+1] = x[n1]
        else:
            u[i+1] = x[n1]
    return u

print(max_len_of_increasing_subseq([1,2,3]))




print(gornerSchema([1, 2, 4], 2))

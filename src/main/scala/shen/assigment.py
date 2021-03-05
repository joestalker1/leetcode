def swap(a, b):
    a = a + b
    b = a - b # b = a
    a = a - b #a = b

def exp_power(a, n):
    if n == 1:
        return a
    if n % 2 == 0:
        d = exp_power(a, n // 2)
        return d * d
    return a * exp_power(a, n - 1)


def mul_mat(mat1, mat2):
    res = [[0] * 2 for _ in range(2)]
    res[0][0] = mat1[0][0] * mat2[0][0] + mat1[0][1] * mat2[1][0]
    res[0][1] = mat1[0][0] * mat2[0][1] + mat1[0][1] * mat2[1][1]
    res[1][0] = mat1[1][0] * mat2[0][0] + mat1[1][1] * mat2[1][0]
    res[1][1] = mat1[1][0] * mat2[0][1] + mat1[1][1] * mat2[1][1]
    return res


def exp_mat_power(m, n):
    if n == 1:
        return m
    if n % 2 == 0:
        new_mat = exp_mat_power(m, n // 2)
        return mul_mat(new_mat, new_mat)
    return mul_mat(m, exp_mat_power(m, n - 1))

def gcd(a, b):
    m = a
    n = b
    while m != 0 and n != 0:
        if m >= n:
            m = m % n
        else:
            n = n % m
    if m == 0:
        return n
    return m

def ext_gcd(a, b):
    # m = p * a + q * b
    # n = r * a + s * b
    m = a
    n = b
    p = 1
    q = 0
    r = 0
    s = 1
    while m != 0 and n != 0:
        if m >= n:


def fact(n):
    if n == 1:
        return n
    return n * fact(n-1)

print(gcd(10, 15))
#print(fact(5))
#print(exp_power(2, 4, 0))

#mat = [[1,1],[1,0]]
#print(exp_mat_power(mat, 6)[0][0])




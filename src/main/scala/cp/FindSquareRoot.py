def find_square_root(s):
    e = 0.000001
    a = s / 100
    while abs(s - (a * a)) > e:
        a = (a + s / a) / 2
        print(a)
    return a

print(find_square_root(5))
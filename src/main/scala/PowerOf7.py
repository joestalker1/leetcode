def power_of(number):
    res = 1
    a = 7
    i = 1#start from 1
    while res <= number:
        if i % 2 == 0:
            a = a * a
        else:
            res *= a
        i += 1
    return res / a == number

print(power_of(343))
print(power_of(7))


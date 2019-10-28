def power_of(number, base):
    if number <= 0:
        return None
    a1 = 1
    a2 = base
    i = 1#start from 1
    c = 0 #iteraiton counter
    #find lower and upper bounds: lower <= number <= upper
    while max(a1, a2) < number:
        if i % 2 == 0:
            a2 = a2 * a2
        else:
            a1 *= a2
        i += 1
        c += 1
    min_a = min(a1, a2)
    #it may be optimize
    while min_a < number:
        min_a *= base
        c += 1
    return (number == min_a, c)


x = 7
for _ in range(10):
    print('{} {}'.format(x, power_of(x, 7)))
    x *= 7

def slow_power_of(number, base):
    a = 1
    c = 0
    while a < number:
        a *= base
        c += 1
    return (a == number, c)

a = 3928392938298392839283928392928398928329232323232323232323232232
print(power_of(a, 7))
print(slow_power_of(a, 7))


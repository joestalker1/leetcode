from math import ceil

def fraction(a, b):
    denominators = []


    while a != 0:
        denominators.append(ceil(b / a))
        a, b = (-b) % a, b * ceil(b / a)

    return denominators


print(fraction(4,13))
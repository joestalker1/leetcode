import random


def perecentail(arr, h, k):
    m = 0
    for a in arr:
        if a > m and random.random() > (1 - h / k):
            m += 1
        elif a < m and random.random() < h / k:
            m -= 1
    return m


print(perecentail([1, 2, 3, 4, 5, 6], 1, 2))

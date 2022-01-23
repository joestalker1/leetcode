import random
import math

def ch(key, num_buckets):
    random.seed(key)
    j = 0
    b = -1
    while j < num_buckets:
        b = j
        r = random.randint(0,num_buckets)
        if r > 0:
            j = math.floor((b + 1)/r)
    return b

for i in range(10):
    print(ch(1, 5))

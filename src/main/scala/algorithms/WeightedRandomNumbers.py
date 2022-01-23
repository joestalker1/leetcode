import random
import collections
# weight is sorted in decreasing order of weight
def gen_rand(weight):
    sum_weight = sum([w[1] for w in weight])
    rnd = random.randint(0, sum_weight-1)
    for i in range(len(weight)):
        if rnd < weight[i][1]:
            return weight[i][0]
        rnd -= weight[i][1]
    return -1


freq = collections.defaultdict(int)
for i in range(1000):
    b = gen_rand([(1,4),(2,4),(3,2)])
    freq[b] += 1

print(freq)


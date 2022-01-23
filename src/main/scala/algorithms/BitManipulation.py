def bits(x, k):
    if x & ((pow(2, k)) - 1) == 0:
        print("{} divided by 2".format(x))

    if x & (x - 1) == 0:
        print("{} is the power of 2".format(x))

    a = x ^ (1 << k)

    c = a & (~x)
    z = 0
    while (z - x) & x:
        z = (z - x) & x


def countGrid(color):
    count = 0
    for i in range(0, len(color) - 1):
        for j in range(i + 1, len(color)):
            count_of_subgrids = countSubgrids(color, i, j)
            count += count_of_subgrids * (count_of_subgrids - 1) // 2
    return count


def countSubgrids(color, a, b):
    count = 0
    for i in range(0, len(color)):
        if color[a][i] == 1 and color[b][i] == 1:
            count += 1
    return count


color = [[0, 1, 0, 0, 1],
         [0, 1, 1, 0, 0],
         [1, 0, 0, 0, 0],
         [0, 1, 1, 0, 1],
         [0, 0, 0, 0, 0]]


def optimalSelection(price):
    k = len(price)
    n = len(price[0])
    total = [0] * (1 << k)#number of the subset permutations
    for i in range(0, len(total)):
        total[i] = [0] * n
    for i in range(0, k):
        total[1 << i][0] = price[i][0]

    for d in range(1, n):#days
        for s in range(0, 1 << k): # the subset permutations
            total[s][d] = total[s][d - 1]
            for x in range(0, k):
                if s & (1 << x):
                    total[s][d] = min(total[s][d], total[s ^ (1 << x)][d - 1] + price[x][d])
    return total[(1 << k) - 1][n - 1]

def elevator(weight, x):
    n = len(weight)
    best = [0] * (1 << n)
    for i in range(0, len(best)):
        best[i] = [0, 0]
    best[0] = [1, 0] #[num of rides, min weight in a last ride]
    for s in range(1, 1 << n):
        best[s] = [n + 1, 0]
        for p in range(0, n):
            if s & (1 << p):
                opt = best[s ^ (1 << p)]
                if opt[1] + weight[p] <= x:
                    opt[1] += weight[p]
                else:
                    opt[0] += 1
                    opt[1] = weight[p]
                if best[s][0] > opt[0]:
                    best[s] = opt
    return None #??


weight = [2,3,3,5,6]
print(elevator(weight, 10))



#product = [[6, 9, 5, 2, 8, 9, 1, 6], [8, 2, 6, 2, 7, 5, 7, 2], [5, 3, 9, 7, 3, 5, 1, 4]]
#print(optimalSelection(product))

# print(countGrid(color))


# bits(3, 2)

def steps(n):
    # set to max steps for i
    distance = [i - 1 for i in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(int(i ** 0.5), 1, -1):
            if i % j == 0:
                distance[i] = min(distance[i], distance[i // j] + 1)
        distance[i] = min(distance[i], distance[i - 1] + 1)

    return distance[-1]



print(steps(10))
def max_score(scores):
    sum_scores = [0] * (len(scores) + 1)
    for i in range(len(scores)):
        sum_scores[i + 1] = sum_scores[i] + scores[i]
    len_of_mural = len(scores) // 2
    if len(scores) % 2 == 1:
        len_of_mural += 1

    j = 0
    max_sum = 0
    while j + len_of_mural < len(sum_scores):
        s = sum_scores[j + len_of_mural] - sum_scores[j]
        if s > max_sum:
            max_sum = s
        j += 1
    return max_sum

# print(max_score([6,1,6]))
# print(max_score([]))
n = int(input())
for i in range(n):
    t = int(input())
    s = input()
    scores = list(map(lambda x: int(x), s))
    print("Case #{}: {}".format(i+1, max_score(scores)), end='\r\n')

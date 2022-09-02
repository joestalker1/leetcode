def process(case_num):
    (candy_bags, kids) = tuple(map(int, input().split()))
    candies = list(map(int, input().split()))
    remain = sum(candies) % kids
    print(f'Case #{case_num}: {remain}')


t = int(input())
for i in range(1, t + 1):
    process(i)


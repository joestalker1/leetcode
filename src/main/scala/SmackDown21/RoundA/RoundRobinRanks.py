def run_task():
    t = int(input().strip())
    for _ in range(t):
        arr = input().strip().split(' ')
        n = int(arr[0])
        k = int(arr[1])
        wins = n* (n-1) // 2
        score = n - k
        low_score = score*(score - 1)//2
        k_score = (wins - low_score) * 2
        print(k_score)


run_task()

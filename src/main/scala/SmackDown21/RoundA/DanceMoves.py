def input_data():
    t = int(input().strip())
    for _ in range(t):
        arr = input().strip().split(' ')
        x = abs(int(arr[0]))
        y = abs(int(arr[1]))
        d = 0
        if x < y:
            d = (y-x) // 2
            if d * 2 < y:
                d += 1
        else:
            d = abs(x-y)
        print(d)

input_data()
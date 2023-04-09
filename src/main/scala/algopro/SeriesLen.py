def solve():
    cur_len = 0
    while True:
        n = int(input())
        if n == 0:
            return cur_len
        cur_len += 1

        
print(solve())
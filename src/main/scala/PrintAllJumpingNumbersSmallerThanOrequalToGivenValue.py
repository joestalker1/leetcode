def jumpingNumber(n):
    res = []

    def bfs(a, res):
        q = [a]
        while q:
            x = q.pop(0)

            if x <= n:
                res.append(x)
                last_digit = x % 10
                if last_digit == 0:
                    q.append(10 * x + 1)
                elif last_digit == 9:
                    q.append(10 * x + last_digit - 1)
                else:
                    q.append(10 * x + last_digit - 1)
                    q.append(10 * x + last_digit + 1)

    for i in range(1, 10):
        bfs(i, res)

    return sorted(res)


print(jumpingNumber(20))

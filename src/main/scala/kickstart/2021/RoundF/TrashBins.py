from math import inf


def calc_path(s):
    left = [inf] * len(s)
    left[0] = 0 if s[0] == '1' else inf
    for i in range(1, len(s)):
        if s[i] == '1':
            left[i] = i
        else:
            left[i] = left[i - 1]
    right = [inf] * len(s)
    right[-1] = (len(s) - 1 if s[-1] == '1' else inf)
    for i in range(len(s) - 2, -1, -1):
        if s[i] == '1':
            right[i] = i
        else:
            right[i] = right[i + 1]
    sum_path = 0
    for i in range(len(s)):
        sum_path += min(abs(left[i] - i), abs(i - right[i]))
    return sum_path


def input_data():
    t = int(input())
    for i in range(1, t + 1):
        n = input()
        n = n.strip()
        n = int(n)
        s = input()
        s = s.strip()
        sum_path = calc_path(s)
        print('Case #{}: {}'.format(i, sum_path))


input_data()

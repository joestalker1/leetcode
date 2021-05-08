def bin_search(a1, a2):
    l = a1
    while a1 <= a2:
        m = a1 + (a2 - a1) // 2
        if m == l:
            return linear_search(a1, a2)
        print(m)
        answer = input()
        if answer == 'TOO_BIG':
            a2 = m - 1
        elif answer == 'TOO_SMALL':
            a1 = m + 1
        else:
            return
    return



def linear_search(a1, a2):
    for a in range(a1 + 1, a2 + 1):
        print(a)
        answer = input()
        if answer == 'CORRECT':
            return


t = int(input())
for i in range(t):
    s = input()
    arr = s.split(' ')
    a = int(arr[0])
    b = int(arr[1])
    tries = int(input())
    bin_search(a, b)


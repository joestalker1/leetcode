def solve():
    ch = input()
    if 'a' <= ch <= 'z':
        d = ord(ch) - ord('a')
        print(chr(ord('A') + d))
    else:
        print(ch)

solve()

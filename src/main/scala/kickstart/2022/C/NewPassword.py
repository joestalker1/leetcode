# At least 7 characters.
# At least one uppercase English alphabet letter.
# At least one lowercase English alphabet letter.
# At least one digit.
# At least one special character. There are four special characters: #, @, *, and &.
def solve():
    n = int(input().strip())
    for t in range(1, n+1):
        input()
        passw = input().strip()
        up_cnt = 0
        lw_cnt = 0
        dig_cnt = 0
        spec_cnt = 0
        spec_char = ['#','@','*','&']
        for ch in passw:
            if ch.isdigit():
                dig_cnt += 1
            elif ch.isalpha() and ch.isupper():
                up_cnt += 1
            elif ch.isalpha() and ch.islower():
                lw_cnt += 1
            elif ch in spec_char:
                spec_cnt += 1
        if dig_cnt == 0:
            passw += '1'
        if up_cnt == 0:
            passw +='A'
        if lw_cnt == 0:
            passw += 'a'
        if spec_cnt == 0:
            passw += '@'
        if len(passw) < 7:
            need = 7 - len(passw)
            passw += ('1'*need)
        print('Case #{}: {}'.format(t, passw))

solve()


def rand5():
    return 0

def rand7():
    r1, r2 = rand5(), rand5()
    if r2 <= 3:
        return r1
    elif r2 == 4:
        if r1 <= 3:
            return 6
        else:
            return rand7()
    else: # r2 == 5
        if r1 <= 3:
            return 7
        else:
            return rand7()
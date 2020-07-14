def binString(S, i, res):
    if i == len(S):
        res.append(''.join(S))
        return
    if S[i] == '?':
        S[i] = '1'
        binString(S,i+1, res)

        S[i] = '0'
        binString(S, i+1, res)
        S[i] = '?'
    else:
        binString(S, i+1, res)

res = []
binString(list("1??0?101"), 0, res)
print(res)
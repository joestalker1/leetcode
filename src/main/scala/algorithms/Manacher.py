def manacher(S):
    A = '@#' + '#'.join(S) + '#$'
    Z = [0] * len(A)
    center = 0
    right = 0
    for i in range(1, len(A) - 1):
        if i < right:
            Z[i] = min(right - i, Z[2 * center - i])
        while A[i + Z[i] + 1] == A[i - Z[i] - 1]:
            Z[i] += 1
        if i + Z[i] > right:
            center = i
            right = i + Z[i]
    return Z[2:-2:2]

print(manacher('AA'))
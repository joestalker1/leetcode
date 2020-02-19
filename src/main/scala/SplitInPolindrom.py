def is_palindrome(s):
    return s == s[::-1]

def split_into_palindromes(s):
    A = [[None for _ in range(len(s))] for _ in range(len(s))]

    # Set all substrings of length 1 to be true
    for i in range(len(s)):
        A[i][i] = True

    # Try all substrings of length 2
    for i in range(len(s) - 1):
        A[i][i + 1] = s[i] == s[i + 1]

    i, k = 0, 3
    while k <= len(s):
        while i < (len(s) - k + 1):
            j = i + k - 1
            A[i][j] = A[i + 1][j - 1] and s[i] == s[j]
            i += 1
        k += 1
        i = 0
    #P[i] = max(P[j]+1), 0...j
    P = [None for _ in range(len(s) + 1)]
    P[0] = []
    for i in range(len(P)):
        for j in range(i):
            matrix_i = i - 1
            #consider max(A[0][i-1],A[1][i-2],A[i-1][i-1])+1
            if A[j][matrix_i]:
                if P[i] is None or (len(P[j]) + 1 < len(P[i])):
                    P[i] = P[j] + [s[j:i]]

    return P[-1]

print(split_into_palindromes('racecarannakayak'))
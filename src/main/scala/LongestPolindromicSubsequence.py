def is_palindrome(s):
    return s == s[::-1]

def generate_subsequences(s):
    # if s is empty, return ['']
    if s == '':
        return ['']

    result = []
    # cut first char and call it recursively
    rest = generate_subsequences(s[1:])
    # extend result with res
    result.extend(rest)
    # to each subseq to prepend by s[0]
    result.extend([s[0] + subseq for subseq in rest])

    return result

def longest_palindromic_subsequence_naive(s):
    longest = ''
    for subsequence in generate_subsequences(s):
        if is_palindrome(subsequence) and len(subsequence) > len(longest):
            longest = subsequence

    return longest


def longest_palindromic_subsequence(s):
    matrix = [['' for _ in range(len(s))] for _ in range(len(s))]

    for i, char in enumerate(s):
        matrix[i][i] = char

    for i in reversed(range(len(s))):
        for j in range(i + 1, len(s)):
            if s[i] == s[j]:
                matrix[i][j] = s[i] + matrix[i + 1][j - 1] + s[j]
            else:
                matrix[i][j] = max(matrix[i + 1][j], matrix[i][j - 1], key=lambda s: len(s))
    return matrix[0][len(s) - 1]


print(longest_palindromic_subsequence("MAPTPTMTPA"))
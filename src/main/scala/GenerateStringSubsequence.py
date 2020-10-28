def subsequences(s):
    if s == '':
        return ['']

    result = []
    rest = subsequences(s[1:])
    result.extend(rest)
    result.extend([s[0]+ subseq for subseq in rest])
    return result


print(subsequences("xyz"))
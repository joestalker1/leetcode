def rank(s):
    # Characters in order of frequency
    ranked_chars = 'etaoinsrhdlucmfywgpbvkxqjz'
    return sum(s.count(char) * (26 - ranked_chars.index(char))  for char in s if char in ranked_chars)


def xor_decipher(s):
    b = bytearray.fromhex(s)

    results = []
    for char in range(256):
        result = []
        for byte in b:
            result.append(byte ^ char)
        results.append(bytes(result).decode('utf-8', 'ignore'))
    return max(results, key=rank)


print(xor_decipher("7a575e5e5d12455d405e561254405d5f1276535b5e4b12715d565b5c551262405d505e575f"))
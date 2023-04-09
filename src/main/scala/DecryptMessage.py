def test():
    assert decrypt('dnotq') == 'crime', 'test1'
    assert decrypt('flgxswdliefy') == 'encyclopedia', 'test2'
    assert decrypt('') == '', 'test3'


def find_next_code(prev, cur_code):
    q = 1
    while not (97 <= (cur_code + q * 26) - prev <= 122):
        q += 1
    return cur_code + q * 26


def decrypt(word):
    if not word:
        return ''
    if len(word) < 2:
        return chr(ord(word[0]) - 1)
    step2 = [0] * len(word)
    step2[0] = ord(word[0])
    for i in range(1, len(word)):
        step2[i] = find_next_code(step2[i-1], ord(word[i]))
    step3 = [0] * len(word)
    step3[0] = chr(step2[0] - 1)
    for i in range(1, len(word)):
        step3[i] = chr(step2[i] - step2[i-1])
    return ''.join(step3)


print(decrypt('dnotq'))
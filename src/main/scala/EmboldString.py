def embolden(s, lst):
    bitarray = [False for _ in s]

    # Create bitarray of bold sections by checking each substring
    end = 0
    for i in range(len(s)):
        for word in lst:
            if s[i:i + len(word)] == word:
                end = max(end, i + len(word))
        bitarray[i] = end > i

    # Now that we have the bitarray, let's construct the final
    # output string.
    result = ''
    i = 0
    while i < len(s):
        char = s[i]
        if bitarray[i] is True:
            j = i
            while j < len(s) and bitarray[j]:
                j += 1

            # s[i:j] needs to be bolded.
            result += '<b>'
            result += s[i:j]
            result += '</b>'

            # Move i to end of bold section.
            i = j
        else:
            result += char
            i += 1

    return result
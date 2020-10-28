def char_to_sextet(char):
    o = ord(char)
    if 65 <= o <= 90:
        return o - 65
    elif 97 <= o <= 122:
        return o - 71
    elif 48 <= o <= 57:
        return o + 4
    elif char == '+':
        return 62
    elif char == '/':
        return 63
    else:
        raise Exception('Invalid char.')


def convert_base64_to_hex(b):
    # Cut off padding
    padding = b.count('=')
    b = b.rstrip('=')

    # Convert base64 into binary string
    bin_string = ''
    for char in b:
        #convert to sextet and take bin digits from 2 to 7 filling with 0 to the left
        sextet = bin(char_to_sextet(char))[2:].zfill(6)
        bin_string += sextet

    # Discard padding * 2 last digits from string
    #discard zeros from the right
    if padding > 0:
        bin_string = bin_string[:-(padding * 2)]

    # Convert binary string into hex string (oxtets)
    result = ''
    for i in range(0, len(bin_string), 8):
        octet = bin_string[i:i + 8]
        # convert to hex string by discarding the prefix 0x
        result += hex(int(octet, 2))[2:]

    return result


print(convert_base64_to_hex("3q2+7w=="))
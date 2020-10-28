def sextet_to_char(sextet):
    i = int(sextet, 2)
    if 0 <= i <= 25:
        return chr(i + 65)
    elif 26 <= i <= 51:
        return chr(i + 71)
    elif 52 <= i <= 61:
        return str(i - 52)
    elif i == 62:
        return '+'
    elif i == 63:
        return '/'
    else:
        raise Exception('Invalid sextet.')


def convert_hex_to_base64(s):
    b = bytearray.fromhex(s)

    # Convert to bit string.
    bit_string = ''
    for c in b:
        bit_string += bin(c)[2:].zfill(8)

    # Calculate padding and pad rest of string with 0s.
    padding = 6 - len(bit_string) % 6
    bit_string += '0' * padding

    # Break down bit string into sextets and convert to base64 chars.
    result = ''
    for i in range(0, len(bit_string), 6):
        sextet = bit_string[i:i + 6]
        result += sextet_to_char(sextet)

    # Add equal sign padding
    result += '=' * (padding // 2)

    return result


print(convert_hex_to_base64("deadbeef"))
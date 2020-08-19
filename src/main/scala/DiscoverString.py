from collections import defaultdict

def get_digits(string):
    letter_counts = defaultdict(int)
    for char in string:
        letter_counts[char] += 1

    int_counts = {i: 0 for i in range(10)}

    int_counts[0] = letter_counts['z']
    int_counts[2] = letter_counts['w']
    int_counts[4] = letter_counts['u']
    int_counts[6] = letter_counts['x']
    int_counts[8] = letter_counts['g']

    int_counts[3] = letter_counts['h'] - int_counts[8]
    int_counts[5] = letter_counts['f'] - int_counts[4]
    int_counts[7] = letter_counts['s'] - int_counts[6]

    int_counts[1] = letter_counts['o'] - int_counts[0] - int_counts[2] - int_counts[4]
    int_counts[9] = letter_counts['i'] - int_counts[5] - int_counts[6] - int_counts[8]

    return ''.join(str(i) * int_counts[i] for i in range(10))


print(get_digits("niesevehrtfeev"))
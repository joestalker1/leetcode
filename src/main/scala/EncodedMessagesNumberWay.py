from collections import defaultdict

def num_encodings(s):
    # On lookup, this hashmap returns a default value of 0 if the key doesn't exist
    # cache[i] gives us # of ways to encode the substring s[i:]
    cache = defaultdict(int)
    # [i:len(s)] is number of encoded string
    cache[len(s)] = 1 # Empty string is 1 valid encoding

    for i in range(len(s)-1, -1, -1):
        if s[i].startswith('0'):
            cache[i] = 0
        elif i == len(s) - 1:
            cache[i] = 1
        else:
            if int(s[i:i + 2]) <= 26:
                #s[0:2] is not holictic string,so it can't count it as distinct
                #s[0:2]+ s[i+2:] leftover of
                cache[i] = cache[i + 2]
            # s[0:1] + s[i+1:]
            cache[i] += cache[i + 1]
    return cache[0]


print(num_encodings('111'))
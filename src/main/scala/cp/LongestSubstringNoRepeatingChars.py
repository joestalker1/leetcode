#from sets import Set

def longest_substr(s):
    if not s:
        return None
    start = 0
    end = 0
    longest = ''
    char_set = set()

    while end < len(s):
        end += 1
        cur_char = s[end-1]
        if cur_char not in char_set:
            char_set.add(cur_char)
            if end - start > len(longest):
                longest = s[start:end]
            continue
        while start < end - 1:
            if s[start] != cur_char:
                char_set.remove(s[start])
                start+=1
            else:
                start+=1
                break
    return longest

s= "abcadbef"

print(longest_substr(s))


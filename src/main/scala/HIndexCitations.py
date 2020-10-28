def h_index(lst):
    result = 0
    dec_order = list(reversed(sorted(lst)))
    for i, num_citations in enumerate(dec_order):
        if num_citations > i:
            result = i + 1
        else:
            break
    return result


print(h_index([4, 1, 0, 2, 3]))


COLORS = {'R', 'G', 'B'}

def transform(a, b):
    return list(COLORS - {a, b})


def num_remaining(quxes):
    if len(set(quxes)) == 1:
        return len(quxes)

    results = []
    # try to transform any i and i+1
    for i, pair in enumerate(zip(quxes, quxes[1:])):
        if pair[0] != pair[1]:
            results.append(num_remaining(quxes[:i] + transform(*pair) + quxes[i + 2:]))

    return min(results)


print(num_remaining(['R', 'G', 'B', 'G', 'B']))
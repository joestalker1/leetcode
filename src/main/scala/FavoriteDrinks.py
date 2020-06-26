from itertools import combinations


def satisfies(option, preferences):
    return all(set(c).intersection(option) for c in preferences.values())


def make_drinks(preferences):
    customers = preferences.keys()
    drinks = set([x for y in preferences.values() for x in y])

    for i in range(1, len(customers) + 1):
        options = combinations(drinks, i)
        for option in options:
            if satisfies(option, preferences):
                return i


print(make_drinks({
    0: [0, 3],
    1: [1, 4],
    2: [5, 6],
    3: [4, 5],
    4: [3, 5],
    5: [2, 6]
}))

def interval_union(intervals):
    starts = [(x, 1) for x, y in intervals]
    ends = [(y, -1) for x, y in intervals]

    sorted_events = sorted(starts + ends, key=lambda k: (k[0], -k[1]))
    cnts = 0

    start, end = -1, -1
    out = []

    for i in range(len(sorted_events)):
        if sorted_events[i][1] == 1:
            cnts += 1
            if cnts == 1:
                start = sorted_events[i][0]
        else:
            cnts -= 1
            if cnts == 0:
                end = sorted_events[i][0]
                if end > start:
                    out.append([start, end])

    return out


def interval_intersection(intervals):
    starts = [(x, 1) for x, y in intervals]
    ends = [(y, -1) for x, y in intervals]

    sorted_events = sorted(starts + ends, key=lambda k: (k[0], -k[1]))
    cnts = 0

    start, end = -1, -1
    out = []

    for i in range(len(sorted_events)):
        if sorted_events[i][1] == 1:
            cnts += 1
            if cnts == 2:
                start = sorted_events[i][0]
        else:
            cnts -= 1
            if cnts == 1:
                end = sorted_events[i][0]
                if end > start:
                    out.append([start, end])

    return out


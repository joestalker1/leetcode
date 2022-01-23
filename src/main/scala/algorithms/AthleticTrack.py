import math

def length(a, b):
    lo = 0.0
    hi = 400.0
    l = 0
    w = 0
    while abs(lo - hi) > 10**9:
        l = (lo + hi) / 2.0
        w = b * l / a
        expected_arc = (400 - 2.0 * l) / 2.0
        half_l = 0.5 * l
        half_w = 0.5 * w
        r = math.sqrt(half_l * half_l + half_w * half_w)
        angle = 2.0 * math.atan(half_w / half_l) * 180.0 / math.pi
        this_arc = angle / 360.0 * math.pi * (2.0 * r)
        if this_arc > expected_arc:
            hi = l
        else:
            lo = l
    return (l,w)

        



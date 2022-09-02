def read_console():
    buf = []
    s = input()
    while s:
        s = s.strip()
        if s:
            buf.append(s)
        s = input()
    return buf


def write_console(buf):
    for s in buf:
        print(s)


def read_file(path):
    with open(path) as f:
        buf = []
        s = f.readline()
        while s:
             s = s.strip()
             if s:
                 buf.append(s)
             s = f.readline()
        return buf


def write_file(path, buf):
    with open(path, 'w') as f:
        for s in buf:
            f.write(s)
            f.write('\n')

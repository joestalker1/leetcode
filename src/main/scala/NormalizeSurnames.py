fout = open("output.txt","w+")

with open('australian_last_names.txt') as f:
    for line in f:
        #line = line.strip()
        if len(line) == 0:
            continue
        parts = line.split(" ")
        if len(parts) > 1:
            s = parts[1] + '\n'
        else:
            s = parts[0]
        fout.write(s)
fout.close()



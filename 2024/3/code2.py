gears = {}

with open('3/input.txt') as f:
    lines = f.readlines()
    somme = 0
    for i in range(len(lines)):
        j = 0
        while j < len(lines[0].strip()):
            n = ''
            while lines[i][j].isnumeric():
                n += lines[i][j]
                j += 1
            j += 1
            if n.isnumeric():
                accepted = False
                for b in range(max(i-1, 0), min(i+2, len(lines))):
                    for a in range(max(j-len(n)-2, 0), min(j, len(lines[0].strip()))):
                        c = lines[b][a]
                        if c != '.' and not c.isnumeric():
                            accepted = True
                            if c == "*":
                                if not (b, a) in gears:
                                    gears[(b, a)] = [int(n)]
                                else:
                                    gears[(b, a)].append(int(n))
                            #print(b, a)
                            #print(c)
                if accepted:
                    somme += int(n)
    print(gears)
    gears = [v[0]*v[1] for k, v in gears.items() if len(v) > 1]
    print(gears)
    total_gear = sum(gears)
    print(total_gear)

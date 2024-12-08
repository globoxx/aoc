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
                        #print(c)
                        if c != '.' and not c.isnumeric():
                            accepted = True
                            #print(b, a)
                            #print(c)
                if accepted:
                    somme += int(n)
    print(somme)
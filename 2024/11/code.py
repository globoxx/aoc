def all_pairs(lst):
    if len(lst) <= 1:
        return []
     
    pairs = [(lst[0], x) for x in lst[1:]]
     
    return pairs + all_pairs(lst[1:])

with open('11/input.txt') as f:
    lines = [line.strip() for line in f.readlines()]

    rows_to_insert = []
    for i in range(len(lines)):
        empty = True
        for j in range(len(lines[0])):
            if lines[i][j] == "#":
                empty = False
                break
        if empty:
            rows_to_insert.append(i)
    to_add = 0
    for row in rows_to_insert:
        lines.insert(row+1+to_add, ''.join(["."]*len(lines[0])))
        to_add += 1

    cols_to_insert = []
    for i in range(len(lines[0])):
        empty = True
        for j in range(len(lines)):
            if lines[j][i] == "#":
                empty = False
                break
        if empty:
            cols_to_insert.append(i)
    to_add = 0
    for col in cols_to_insert:
        for i in range(len(lines)):
            line = lines[i]
            line = list(line)
            line.insert(col+to_add, ".")
            line = ''.join(line)
            lines[i] = line
        to_add += 1
        

    galaxies = []
    for i in range(len(lines)):
        for j in range(len(lines[0])):
            c = lines[i][j]
            if c == "#":
                galaxies.append((i, j))

    galaxies_pairs = all_pairs(galaxies)
    dists = []
    for pair in galaxies_pairs:
        p1, p2 = pair
        x1, y1 = p1
        x2, y2 = p2
        dist = abs(x2 - x1) + abs(y2 - y1)
        dists.append(dist)

    print(sum(dists))
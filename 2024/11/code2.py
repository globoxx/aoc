def all_pairs(lst):
    if len(lst) <= 1:
        return []
     
    pairs = [(lst[0], x) for x in lst[1:]]
     
    return pairs + all_pairs(lst[1:])

def count_cross_values(x, y, list_v):
    if x > y:
        x, y = y, x
    count = 0
    for v in list_v:
        if x < v < y:
            count += 1
    return count

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

    cols_to_insert = []
    for i in range(len(lines[0])):
        empty = True
        for j in range(len(lines)):
            if lines[j][i] == "#":
                empty = False
                break
        if empty:
            cols_to_insert.append(i)

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
        count_x = count_cross_values(x1, x2, rows_to_insert)
        count_y = count_cross_values(y1, y2, cols_to_insert)
        dist = abs(x2 - x1) + count_x*999999 + abs(y2 - y1) + count_y*999999
        dists.append(dist)

    print(sum(dists))
with open('1/input.txt') as f:
    lines = f.readlines()
    lines = [[c for c in line if str.isnumeric(c)] for line in lines]
    somme = sum([int(line[0] + line[-1]) for line in lines])
    print(somme)
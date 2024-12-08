colors_available = {
    "blue": 14,
    "red": 12,
    "green": 13
}

with open('2/input.txt') as f:
    lines = f.readlines()
    somme = 0
    for i, line in enumerate(lines):
        id_nb = i+1
        bag = line.split(':')[1]
        use_it = True
        for sub_bag in bag.split(';'):
            for color in sub_bag.split(','):
                color = color.strip()
                color_color = None
                for c in colors_available.keys():
                    if c in color:
                        color_nb = int(color.split(c)[0])
                        if color_nb > colors_available[c]:
                            use_it = False
                        break
        if use_it:
            somme += id_nb
    print(somme)
                

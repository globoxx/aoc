with open('8/input.txt') as f:
    lines = [line.strip() for line in f.readlines()]
    instructions = lines[0]

    goes = {}
    for line in lines[2:]:
        loc = line.split('=')[0].strip()
        left = line.split('=')[1].split(',')[0].strip()[1:]
        right = line.split('=')[1].split(',')[1].strip()[:-1]
        assert loc not in goes
        goes[loc] = (left, right)

    location = "AAA"
    i = 0
    while location != "ZZZ":
        direction = instructions[i]
        if direction == "L":
            location = goes[location][0]
        else:
            location = goes[location][1]
        i += 1
        if i >= len(instructions):
            instructions += instructions

    print(i)
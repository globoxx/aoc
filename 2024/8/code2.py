import math

with open('8/input.txt') as f:
    lines = [line.strip() for line in f.readlines()]
    instructions = lines[0]

    goes = {}
    locations = []
    for line in lines[2:]:
        loc = line.split('=')[0].strip()
        left = line.split('=')[1].split(',')[0].strip()[1:]
        right = line.split('=')[1].split(',')[1].strip()[:-1]
        assert loc not in goes
        goes[loc] = (left, right)
        if loc[-1] == 'A':
            locations.append(loc)
    print(locations)

    all_i = []
    for location in locations:
        i = 0
        while location[-1] != "Z":
            direction = instructions[i]
            if direction == "L":
                location = goes[location][0]
            else:
                location = goes[location][1]
            i += 1
            if i >= len(instructions):
                instructions += instructions
        all_i.append(i)

    print(math.lcm(*all_i))
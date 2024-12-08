with open('6/input.txt') as f:
    lines = [line.strip() for line in f.readlines()]
    time = int(''.join(lines[0].split(':')[-1].split()))
    record = int(''.join(lines[1].split(':')[-1].split()))

    nb_win = 0
    for hold_time in range(1, time):
        time_left = time - hold_time
        speed = hold_time
        distance = speed*time_left
        if distance > record:
            nb_win += 1
    print(nb_win)
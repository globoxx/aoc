import copy
import re

def extract_tuples(text: str):
    text = text.strip().replace("\n", " ")

    return text

def visitate_has_loop(total_text, starting_position=None, direction=None):
    if starting_position is None or direction is None:
        for i in range(len(total_text)):
            for j in range(len(total_text[i])):
                if total_text[i][j] == "^":
                    starting_position = (i, j)
                    direction = (-1, 0)
                    break
                elif total_text[i][j] == "v":
                    starting_position = (i, j)
                    direction = (1, 0)
                    break
                elif total_text[i][j] == "<":
                    starting_position = (i, j)
                    direction = (0, -1)
                    break
                elif total_text[i][j] == ">":
                    starting_position = (i, j)
                    direction = (0, 1)
                    break
    
    (i, j) = starting_position
    starting_direction = direction
    
    positions = []
    hash_positions = set()
    while True:
        i += direction[0]
        j += direction[1]
        if (i, j, direction[0], direction[1]) in hash_positions:
            print('loop')
            return True, None, None, None
        positions.append((i, j, direction[0], direction[1]))
        if i >= len(total_text) or j >= len(total_text[i]) or i < 0 or j < 0:
            positions.pop()
            break
        elif total_text[i][j] == "#":
            i -= direction[0]
            j -= direction[1]
            positions.pop()

            if direction == (0, -1):
                direction = (-1, 0)
            elif direction == (1, 0):
                direction = (0, -1)
            elif direction == (0, 1):
                direction = (1, 0)
            elif direction == (-1, 0):
                direction = (0, 1)
        else:
            hash_positions.add((i, j, direction[0], direction[1]))

    unique_positions = set(positions)
    visited_positions = [(u[0], u[1]) for u in unique_positions]
    visited_positions = set(visited_positions)
    return False, visited_positions, starting_position, starting_direction

with open('2025/6/input.txt') as f:
    lines = f.readlines()
    total_text = [extract_tuples(line) for line in lines]
    
    has_loop, visited_positions, starting_position, direction = visitate_has_loop(total_text)

    n = 0
    k = 0
    total_text = [list(t) for t in total_text]
    for i, j in visited_positions:
        if total_text[i][j] != ".":
            continue
        total_text[i][j] = "#"
        has_loop, _, _, _ = visitate_has_loop(total_text, starting_position=starting_position, direction=direction)
        if has_loop:
            n += 1
            
        total_text[i][j] = "."
        k += 1
        print(k / len(visited_positions) * 100)
    
    print(n)
            
    

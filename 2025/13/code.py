import path
import sys
import re

directory = path.Path(__file__).absolute()
sys.path.append(directory.parent.parent)

from utils import Board, Point

def det(a, b):
    return a.x * b.y - a.y * b.x

def find_min_translations(translation_a, translation_b, target):
    det_ab = det(translation_a, translation_b)
    if det_ab == 0:
        return None, None  # a et b son collinéaires, heureusement ça n'arrive pas on dirait

    det_target_b = det(target, translation_b)
    det_a_target = det(translation_a, target)

    n = det_target_b / det_ab
    m = det_a_target / det_ab

    if n.is_integer() and m.is_integer(): # On veut des solutions entières uniquement
        return int(n), int(m)
    else:
        return None, None

with open('2025/13/input.txt') as f:
    lines = [line.strip() for line in f.read().strip().splitlines()]
    lines = [line for line in lines if line]
    
    m = [lines[i:i+3] for i in range(0, len(lines), 3)]
    machines = {}
    for i, machine in enumerate(m):
        machine_id = i
        numbers = re.findall(r'\d+', machine[0])
        machines[machine_id] = {'A': (int(numbers[0]), int(numbers[1]))}
        numbers = re.findall(r'\d+', machine[1])
        machines[machine_id]['B'] = (int(numbers[0]), int(numbers[1]))
        numbers = re.findall(r'\d+', machine[2])
        machines[machine_id]['C'] = (int(numbers[0]) + 10000000000000, int(numbers[1]) + 10000000000000)
    
    total_tokens = 0
    for machine_id, machine in machines.items():
        moves_a, moves_b = find_min_translations(Point(*machine['A']), Point(*machine['B']), Point(*machine['C']))
        if moves_a is None or moves_b is None:
            print('No solution')
            continue
        tokens = moves_a*3 + moves_b
        print(tokens)
        total_tokens += tokens
    print('total:', total_tokens)
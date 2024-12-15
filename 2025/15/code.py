import path
import sys
import re
from PIL import Image
import numpy as np

directory = path.Path(__file__).absolute()
sys.path.append(directory.parent.parent)

from utils import Board, Point

def flatten(l):
    return [item for sublist in l for item in sublist]

board = None
with open('2025/15/input.txt') as f:
    lines = [line.strip() for line in f.read().strip().splitlines()]
    new_lines = []
    for line in lines:
        line = line.replace('O', '[]')
        line = line.replace('#', '##')
        line = line.replace('.', '..')
        line = line.replace('@', '@.')
        new_lines.append(line)
            
    board = Board(new_lines)
    #board.show()
     
moves = None       
with open('2025/15/input2.txt') as f:
    moves = [line.strip() for line in f.read().strip().splitlines()]
    moves = flatten(moves)
    print(len(moves))
    print(moves)
        
robot = board.get_positions('@')[0]
walls = board.get_positions('#')

for k, move in enumerate(moves):
    rocks = board.get_positions('[')
    rocks += board.get_positions(']')

    if move == '^':
        direction = Point(-1, 0)
    elif move == 'v':
        direction = Point(1, 0)
    elif move == '<':
        direction = Point(0, -1)
    elif move == '>':
        direction = Point(0, 1)
    
    new_pos = robot + direction
    if new_pos in walls: # Mur en face
        continue
    elif new_pos in rocks: # Bloc en face
        if move == '^' or move == 'v':
            rock_char = board.get_at(new_pos)
            dir_other_char = Point(0, 1) if rock_char == '[' else Point(0, -1)
            all_rocks_impacted = [(new_pos, new_pos + dir_other_char)]
            for a, b in all_rocks_impacted: # Pratique risquée de parcourir une liste que je modifie mais ici plutôt safe car je ne rajoute qu'à la fin
                if board.get_at(a + direction) in ['[', ']']:
                    impacted_char = board.get_at(a + direction)
                    if impacted_char == '[':
                        all_rocks_impacted.append((a + direction, a + direction + Point(0, 1)))
                    else:
                        all_rocks_impacted.append((a + direction, a + direction + Point(0, -1)))
                if board.get_at(b + direction) in ['[', ']']:
                    impacted_char = board.get_at(b + direction)
                    if impacted_char == '[':
                        all_rocks_impacted.append((b + direction, b + direction + Point(0, 1)))
                    else:
                        all_rocks_impacted.append((b + direction, b + direction + Point(0, -1)))
                    
            can_move = True    
            for a, b in all_rocks_impacted:
                if a + direction in walls or b + direction in walls:
                    can_move = False
                    break
            if not can_move:
                continue
            
            for i in range(len(all_rocks_impacted)):
                a, b = all_rocks_impacted[i]
                if a.x > b.x:
                    all_rocks_impacted[i] = (b, a)
            
            for a, b in all_rocks_impacted:
                board.set_at(a, '.')
                board.set_at(b, '.')
            for a, b in all_rocks_impacted:
                board.set_at(a + direction, '[')
                board.set_at(b + direction, ']')
            robot = new_pos
            board.set_at(robot - direction, '.')
            board.set_at(robot, '@')
        else:
            rock_char = board.get_at(new_pos)
            rock_other_char = '[' if rock_char == ']' else ']'
            dir_other_char = Point(0, 1) if rock_char == '[' else Point(0, -1)
            all_rocks_parts = board.get_continuous_positions(new_pos, direction, [rock_char, rock_other_char])
            if (all_rocks_parts[-1] + direction) in walls:
                continue
            for rock in all_rocks_parts:
                board.set_at(rock, '.')
            for i, rock in enumerate(all_rocks_parts):
                if i % 2 == 0:
                    board.set_at(rock + direction, rock_char)
                else:
                    board.set_at(rock + direction, rock_other_char)
            robot = new_pos
            board.set_at(robot - direction, '.')
            board.set_at(robot, '@')
    else: # Rien en face
        robot = new_pos
        board.set_at(robot - direction, '.')
        board.set_at(robot, '@')
        
board.show()

total = 0
for rock in board.get_positions('['):
    coords = rock.x + rock.y * 100
    total += coords
    
print(total)
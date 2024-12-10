import path
import sys
from random import *

directory = path.Path(__file__).absolute()
sys.path.append(directory.parent.parent)

from utils import Board, Point


with open('2025/10/input.txt') as f:
    lines = [line.strip() for line in f.read().strip().splitlines()]
    lines = [[int(x) for x in line] for line in lines]
    board = Board(lines)
    
    starts = board.get_positions(0)
    
    all_paths = set()
    for start in starts:
        summits_achieved = set()
        for _ in range(5000):
            current_path = [start]
            current = start
            v = board.get_at(current)
            while True:
                adjacents = board.get_adjacent_positions(current)
                nexts = [pos for pos in adjacents if board.get_at(pos) == v + 1]
                if not nexts:
                    break
                current = choice(nexts)
                v = board.get_at(current)
                current_path.append(current)
                if v == 9 and tuple(current_path) not in all_paths:
                    all_paths.add(tuple(current_path))
                    summits_achieved.add(current)
                    break
    print(len(all_paths))
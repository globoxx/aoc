import path
import sys
import re
import numpy as np

directory = path.Path(__file__).absolute()
sys.path.append(directory.parent.parent)

from utils import Board, Point

with open('2025/18/input.txt') as f:
    lines = [line.strip() for line in f.read().strip().splitlines()]     
    print(lines)
    points = []
    for line in lines:
        x, y = map(int, line.split(','))
        points.append(Point(x, y))
    print(points)
    
    max_x = max(point.x for point in points)
    max_y = max(point.y for point in points)
    
    new_lines = []
    for y in range(max_y + 1):
        new_line = '.' * (max_x + 1)
        new_lines.append(new_line)
    print(new_lines)
    
    start = Point(0, 0)
    end = Point(max_y, max_x)
    print(start, end)
    
    board = Board(new_lines)
    
    shortest_path = []
    for k, point in enumerate(points):
        board.set_at(point, '#')
        if shortest_path and point not in shortest_path:
            continue
        
        shortest_path = board.get_shortest_path_astar(start, end, walls=set(board.get_positions('#')))

        print(k+1, len(shortest_path))
        if len(shortest_path) == 0:
            print((point.y, point.x))
            break
    
    
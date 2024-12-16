import path
import sys
import re
import numpy as np

directory = path.Path(__file__).absolute()
sys.path.append(directory.parent.parent)

from utils import Board, Point

def get_score_path(path: list[Point], start: Point) -> int:
    scores = []
    direction = Point(0, 1)
    for i, point in enumerate(path):
        direction_taken = point - path[i - 1] if i > 0 else point - start
        angle = np.arctan2(direction_taken.y, direction_taken.x) - np.arctan2(direction.y, direction.x)
        angle = abs(np.rad2deg(angle))
        if angle > 180:
            angle = 360 - angle
        assert angle == 0 or angle == 90
        score = 1 + int(angle / 90)*1000

        scores.append(score)
        direction = direction_taken
    return scores

with open('2025/16/input.txt') as f:
    lines = [line.strip() for line in f.read().strip().splitlines()]     
    board = Board(lines)
    #board.show()
    
    start = board.get_positions('S')[0]
    end = board.get_positions('E')[0]
    
    shortest_paths = board.get_shortest_paths_astar(start, end, board.get_positions('#'))
    
    new_board = Board(lines)
    points_in_path = set()
    for shortest_path in shortest_paths:
        for point in shortest_path:
            points_in_path.add(point)
    print(len(points_in_path))
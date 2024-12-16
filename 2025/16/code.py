import path
import sys
import re
from PIL import Image
import numpy as np

directory = path.Path(__file__).absolute()
sys.path.append(directory.parent.parent)

from utils import Board, Point

def get_score_path(path: list[Point], start: Point, board: Board) -> int:
    scores = []
    # direction = east
    direction = Point(0, 1)
    for i, point in enumerate(path):
        direction_taken = point - path[i - 1] if i > 0 else point - start
        # calcule difference in degrees between direction_taken and direction
        angle = np.arctan2(direction_taken.y, direction_taken.x) - np.arctan2(direction.y, direction.x)
        # convert to degrees
        angle = abs(np.rad2deg(angle))
        if angle > 180:
            angle = 360 - angle
        score = 1 + int(angle / 90)*1000
        if score > 2000:
            print('wtf-------------------------------------------------------------------------')
        scores.append(score)
        direction = direction_taken
    return scores

with open('2025/16/x2.txt') as f:
    lines = [line.strip() for line in f.read().strip().splitlines()]     
    board = Board(lines)
    #board.show()
    
    start = board.get_positions('S')[0]
    end = board.get_positions('E')[0]
    
    
    shortest_paths = board.get_all_shortest_paths(start, end, board.get_positions('#'))
    '''
    shortest_path = shortest_paths[0]
    scores = get_score_path(shortest_path, start=start, board=board)
    print("Path length:", len(shortest_path))
    print(scores)
    print(sum(scores)-1)
    new_board = Board(lines)
    for point in shortest_path:
        new_board.set_at(point, 'X')
    new_board.show()
    '''
    
    print(len(shortest_paths))
    
    new_board = Board(lines)
    points_in_path = set()
    for shortest_path in shortest_paths:
        for point in shortest_path:
            points_in_path.add(point)
    print(len(points_in_path))
    for point in points_in_path:
        new_board.set_at(point, 'O')
    new_board.show()
    
    
    '''
    all_paths = board.get_all_paths(start, end, board.get_positions('#'), max_depth=400)
    print(len(all_paths))
    
    all_scores = []
    for i in range(len(all_paths)):
        all_paths[i] = all_paths[i][1:-1]
        
    for p in all_paths:
        scores = get_score_path(p, start=start, board=board)
        print("Path length:", len(p))
        if len(p) == 36:
            print(scores)
        new_board = Board(lines)
        for point in p:
            new_board.set_at(point, 'X')
        new_board.show()
        all_scores.append(scores)
        
    scores = [sum(s) for s in all_scores]
    print(min(scores))
    
    '''
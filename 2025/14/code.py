import path
import sys
import re
from PIL import Image
import numpy as np

directory = path.Path(__file__).absolute()
sys.path.append(directory.parent.parent)

from utils import Board, Point

def simulate(robot, steps, grid_x, grid_y):
    pos = robot[0]
    for _ in range(steps):
        v = robot[1]
        pos += v
        pos = Point(pos.y % grid_y, pos.x % grid_x)
        
    return pos

def get_quadrant(pos, grid_x, grid_y):
    if pos.x < grid_x // 2:
        if pos.y < grid_y // 2:
            return 1
        elif pos.y == grid_y // 2:
            return None
        else:
            return 3
    elif pos.x == grid_x // 2:
        return None
    else:
        if pos.y < grid_y // 2:
            return 2
        elif pos.y == grid_y // 2:
            return None
        else:
            return 4
    
def table_to_image(table, char):
    table = np.array(table)
    
    height, width = table.shape
    image_rgb = np.zeros((height * 10, width * 10, 3), dtype=np.uint8)
    
    point_color = [0, 0, 0]
    background_color = [255, 255, 255]
    
    for i in range(height):
        for j in range(width):
            if table[i, j] == char:
                image_rgb[
                    i*10:(i+1)*10, 
                    j*10:(j+1)*10
                ] = point_color
            else:
                image_rgb[
                    i*10:(i+1)*10, 
                    j*10:(j+1)*10
                ] = background_color
    
    image = Image.fromarray(image_rgb)
    return image

with open('2025/14/input.txt') as f:
    lines = [line.strip() for line in f.read().strip().splitlines()]
    
    robots = []
    for line in lines:
        parts = line.split()
        px, py = map(int, re.findall(r'-?\d+', parts[0]))
        vx, vy = map(int, re.findall(r'-?\d+', parts[1]))
        robots.append((Point(py, px), Point(vy, vx)))
        
    all_positions = {quadrant: [] for quadrant in range(1, 5)}
    for step in range(10000):
        grid_to_print = [['.' for _ in range(101)] for _ in range(103)]
        for i, robot in enumerate(robots):
            pos = simulate(robot, 1, 101, 103)
            robot[0].x = pos.x
            robot[0].y = pos.y
            quadrant = get_quadrant(pos, 101, 103)
            if quadrant is not None:
                all_positions[quadrant].append(pos)
            grid_to_print[pos.y][pos.x] = '#'
            
        image = tableau_to_image(grid_to_print, '#')
        image.save(f'2025/14/images/{step}.png')
        
        
        if step == 100:
            total = 1
            for quadrant, positions in all_positions.items():
                print(quadrant, positions)
                total *= len(positions)
                
            print(total)
        
        
        
    
    
    
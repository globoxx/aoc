import path
import sys

directory = path.Path(__file__).absolute()
sys.path.append(directory.parent.parent)

from utils import Board, Point, get_oriented_groups

def get_price(region_group: list[Point]):
    area = len(region_group)
    points_perimeter = set()
    for point in region_group:
        for adjacent in point.get_adjacent_positions():
            if adjacent not in region_group:
                dir = adjacent - point
                points_perimeter.add((adjacent, dir))
                
    # perimeter = len(points_perimeter)
    sides = len(get_oriented_groups(list(points_perimeter)))

    print(area, sides)
    return area * sides
    

with open('2025/12/input.txt') as f:
    lines = [line.strip() for line in f.read().strip().splitlines()]
    board = Board(lines)
    
    regions = board.get_regions()
    print(regions)
    
    for region, groups in regions.items():
        for group in groups:
            print(region, get_price(group))
            
    somme = sum(get_price(group) for groups in regions.values() for group in groups)
    print(somme)
import path
import sys

directory = path.Path(__file__).absolute()
sys.path.append(directory.parent.parent)

from utils import Board, Point

def get_groups(points: list[Point]):
    groups = get_oriented_groups([(point, Point(0, 0)) for point in points])
    groups = [[point for point, _ in group] for group in groups]
    return groups

def get_oriented_groups(points: list[tuple[Point, Point]]):
    groups = []
    for point, dir in points:
        adjacent_groups = [group for group in groups if any(point.is_adjacent(other_point) and dir == other_dir for other_point, other_dir in group)]
        if adjacent_groups:
            merged_group = []
            for group in adjacent_groups:
                merged_group.extend(group)
                groups.remove(group)
            
            merged_group.append((point, dir))
            groups.append(merged_group)
        else:
            groups.append([(point, dir)])
    return groups

def get_regions(board: Board):
    regions = {}
    
    for p, v in board.board.items():
        if v in regions:
            regions[v].append(p)
        else:
            regions[v] = [p]
            
    regions_precised = {}
    for region, points in regions.items():
        groups = get_groups(points)
        regions_precised[region] = groups
            
    return regions_precised

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
    
    regions = get_regions(board)
    print(regions)
    
    for region, groups in regions.items():
        for group in groups:
            print(region, get_price(group))
            
    somme = sum(get_price(group) for groups in regions.values() for group in groups)
    print(somme)
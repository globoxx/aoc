import path
import sys

directory = path.Path(__file__).absolute()
sys.path.append(directory.parent.parent)

from utils import Board, Point

with open('2025/8/input.txt') as f:
    lines = [line.strip() for line in f.read().strip().splitlines()]
    board = Board(lines)
    print(board)
    
    freqs = {}
    for y in range(len(lines)):
        for x in range(len(lines[y])):
            c = lines[y][x]
            if c != '.' and c not in freqs:
                freqs[c] = [Point(y, x)]
            elif c != '.':
                freqs[c].append(Point(y, x))
                
    print(freqs)
    
    antinodes = {k: [] for k in freqs.keys()}
    for freq, positions in freqs.items():
        for pos1 in positions:
            for pos2 in positions:
                if pos1 != pos2:
                    diff = pos1 - pos2
                    
                    antinodes[freq].append(pos1)
                    antinodes[freq].append(pos2)
                    
                    pos_antinode = pos1 + diff
                    while pos_antinode.is_in_grid(lines):
                        antinodes[freq].append(pos_antinode)
                        pos_antinode = pos_antinode + diff
                        
                    pos_antinode  = pos2 - diff
                    while pos_antinode.is_in_grid(lines):
                        antinodes[freq].append(pos_antinode)
                        pos_antinode = pos_antinode - diff
    
    print(antinodes)
    
    unique_antinodes_positions = []
    for freq, positions in antinodes.items():
        for pos in positions:
            if pos not in unique_antinodes_positions:
                unique_antinodes_positions.append(pos)
                
    print(unique_antinodes_positions)
    print(len(unique_antinodes_positions))
                    
    

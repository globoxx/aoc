class Point:
    def __init__(self, y, x):
        self.x = x
        self.y = y
        
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    
    def __add__(self, other):
        return Point(self.y + other.y, self.x + other.x)
    
    def __sub__(self, other):
        return Point(self.y - other.y, self.x - other.x)
        
    def __hash__(self):
        return hash((self.x, self.y))
        
    def __repr__(self):
        return f'({self.x}, {self.y})'
    
    def manhattan_distance(self, other):
        return abs(self.x - other.x) + abs(self.y - other.y)
    
    def is_adjacent(self, other):
        return self.manhattan_distance(other) == 1
    
    def is_diagonal(self, other):
        return self.manhattan_distance(other) == 2
    
    def is_in_grid(self, grid):
        return 0 <= self.y < len(grid) and 0 <= self.x < len(grid[0])
    
    
class Board:
    def __init__(self, lines):
        board = {}
        for y in range(len(lines)):
            for x in range(len(lines[y])):
                board[Point(y, x)] = lines[y][x]
        self.board = board
        
    def __repr__(self):
        return str(self.board)
    
    def get_at(self, point):
        if point is not Point:
            point = Point(*point)
        return self.board[point]
    
    def set_at(self, point, value):
        if point is not Point:
            point = Point(*point)
        self.board[point] = value
    
    def get_positions(self, char):
        return [pos for pos, c in self.board.items() if c == char]
    
    def get_continuous_positions(self, start, direction, char=None):
        positions = []
        current = start + direction
        while current in self.board:
            if char is None or self.get_at(current) == char:
                positions.append(current)
                current += direction
            else:
                break
        return positions
    
    def get_adjacent_positions(self, point, with_diagonals=False):
        directions = [Point(0, 1), Point(0, -1), Point(1, 0), Point(-1, 0)]
        if with_diagonals:
            directions += [Point(1, 1), Point(1, -1), Point(-1, 1), Point(-1, -1)]
        return [point + direction for direction in directions]
    
    def get_continuous_path(self, start, char, with_diagonals=False):
        directions = [Point(0, 1), Point(0, -1), Point(1, 0), Point(-1, 0)]
        if with_diagonals:
            directions += [Point(1, 1), Point(1, -1), Point(-1, 1), Point(-1, -1)]
        
        # computes and return all continuous paths from start that contains only the char and are not blocked by another char
        # a path is a list of points
        # a path is not necesseraly a line, it can has turns
        
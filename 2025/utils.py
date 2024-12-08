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
    
    def is_adjacent(self, other):
        return abs(self.x - other.x) + abs(self.y - other.y) == 1
    
    def is_diagonal(self, other):
        return abs(self.x - other.x) == 1 and abs(self.y - other.y) == 1
    
    def is_in_grid(self, grid):
        return 0 <= self.y < len(grid) and 0 <= self.x < len(grid[0])
    
    def manhattan_distance(self, other):
        return abs(self.x - other.x) + abs(self.y - other.y)
    
    
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
    
    def get_positions(self, char):
        return [pos for pos, c in self.board.items() if c == char]
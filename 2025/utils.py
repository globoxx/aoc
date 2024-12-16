import heapq


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
    
    def __mul__(self, scalar):
        return Point(self.y * scalar, self.x * scalar)
    
    def __lt__(self, other):
        return (self.y, self.x) < (other.y, other.x)
        
    def __hash__(self):
        return hash((self.x, self.y))
        
    def __repr__(self):
        return f'({self.x}, {self.y})'
    
    def manhattan_distance(self, other):
        return abs(self.x - other.x) + abs(self.y - other.y)
    
    def chebyshev_distance(self, other):
        return max(abs(self.x - other.x), abs(self.y - other.y))
    
    def is_adjacent(self, other):
        return self.manhattan_distance(other) == 1
    
    def is_diagonal(self, other):
        return self.manhattan_distance(other) == 2
    
    def is_in_grid(self, grid):
        return 0 <= self.y < len(grid) and 0 <= self.x < len(grid[0])
    
    def get_adjacent_positions(self):
        return [Point(self.y, self.x + 1), Point(self.y, self.x - 1), Point(self.y + 1, self.x), Point(self.y - 1, self.x)]
    
    def get_direction(self, other):
        return Point(other.y - self.y, other.x - self.x)
    
    
class Board:
    def __init__(self, lines):
        board = {}
        for y in range(len(lines)):
            for x in range(len(lines[y])):
                board[Point(y, x)] = lines[y][x]
        self.lines = lines
        self.board = board
        self.width = len(lines[0])
        self.height = len(lines)
        
    def __repr__(self):
        return str(self.board)
    
    def get_at(self, point: Point) -> int|str:
        if not isinstance(point, Point):
            point = Point(*point)
        return self.board[point]
    
    def set_at(self, point: Point, value: int|str):
        if not isinstance(point, Point):
            point = Point(*point)
        self.board[point] = value
        
    def show(self):
        for y in range(max(p.y for p in self.board) + 1):
            for x in range(max(p.x for p in self.board) + 1):
                print(self.get_at(Point(y, x)), end='')
            print()
            
    def transpose(self):
        new_board = Board(list(zip(*self.lines)))
        assert new_board.width == self.height and new_board.height == self.width
        return new_board
    
    def flip_vertical(self):
        new_board = Board(self.lines[::-1])
        return new_board
    
    def flip_horizontal(self):
        new_board = Board([line[::-1] for line in self.lines])
        return new_board
    
    def rotate(self, angle=90):
        if angle == 0:
            return self
        elif angle == 90:
            return self.transpose().flip_horizontal()
        elif angle == 180:
            return self.flip_horizontal().flip_vertical()
        elif angle == 270:
            return self.transpose().flip_vertical()
        else:
            raise ValueError('Invalid angle')
        
    def get_positions(self, char: int|str) -> list[Point]:
        return [pos for pos, c in self.board.items() if c == char]
    
    def get_continuous_positions(self, start: Point, direction: Point, chars:list[int|str]|str=None) -> list[Point]:
        if not isinstance(chars, list) and chars is not None:
            chars = [chars]
        positions = [start]
        current = start + direction
        while current in self.board:
            if chars is None or self.get_at(current) in chars:
                positions.append(current)
                current += direction
            else:
                break
        return positions
    
    def get_adjacent_positions(self, point: Point, with_diagonals=False) -> list[Point]:
        directions = [Point(0, 1), Point(0, -1), Point(1, 0), Point(-1, 0)]
        if with_diagonals:
            directions += [Point(1, 1), Point(1, -1), Point(-1, 1), Point(-1, -1)]
        points = [point + direction for direction in directions if point + direction in self.board]
        return points
    
    def get_regions(self) -> dict[int|str, list[list[Point]]]:
        regions: dict[int|str, list[Point]] = {}
        
        for p, v in self.board.items():
            if v in regions:
                regions[v].append(p)
            else:
                regions[v] = [p]
                
        regions_precised = {}
        for region, points in regions.items():
            groups = get_groups(points)
            regions_precised[region] = groups
                
        return regions_precised
    
    def get_pattern(self, start: Point, with_diagonals=False) -> list[Point]:
        regions = self.get_regions()
        
        for _, groups in regions.items():
            for group in groups:
                if start in group:
                    return group
        return []
    
    def get_shortest_path(self, start: Point, end: Point, walls: list[Point], with_diagonals=False) -> list[Point]:
        visited = set()
        queue = [(start, [])]
        
        while queue:
            current, path = queue.pop(0)
            if current == end:
                return path
            
            visited.add(current)
            for adjacent in self.get_adjacent_positions(current, with_diagonals):
                if adjacent in visited or adjacent in walls:
                    continue
                queue.append((adjacent, path + [adjacent]))
        return []
    
    def get_shortest_paths_astar(self, start: Point, end: Point, walls: list[Point]) -> list[list[Point]]:
        # Had to find snippets of code for A* algorithm
        
        def heuristic(a: Point, b: Point) -> int:
            return a.manhattan_distance(b)
        
        class SearchState:
            def __init__(self, point: Point, path: list[Point], direction: Point, rotation_count: int, total_cost: int):
                self.point = point
                self.path = path
                self.direction = direction
                self.rotation_count = rotation_count
                self.total_cost = total_cost
            
            def __lt__(self, other):
                return self.total_cost < other.total_cost
        
        visited = {}
        open_set = []
        all_shortest_paths = []
        min_total_cost = float('inf')
        
        initial_state = SearchState(
            point=start, 
            path=[start], 
            direction=None, 
            rotation_count=0, 
            total_cost=heuristic(start, end)
        )
        heapq.heappush(open_set, initial_state)
        
        while open_set:
            current_state: SearchState = heapq.heappop(open_set)
            
            if current_state.total_cost > min_total_cost:
                break
            
            if current_state.point == end:
                if not all_shortest_paths or current_state.total_cost <= min_total_cost:
                    all_shortest_paths.append(current_state.path)
                    min_total_cost = min(min_total_cost, current_state.total_cost)
                continue
            
            state_key = (current_state.point, current_state.direction)
            if state_key in visited:
                if visited[state_key] < current_state.total_cost:
                    continue
            visited[state_key] = current_state.total_cost
            
            for adjacent in self.get_adjacent_positions(current_state.point):
                if adjacent in walls or adjacent in current_state.path:
                    continue
                
                new_direction = current_state.path[-1].get_direction(adjacent)
                
                rotation_count = current_state.rotation_count
                if current_state.direction and new_direction != current_state.direction:
                    rotation_count += 1
                
                base_cost = len(current_state.path)
                rotation_penalty = rotation_count * 1000
                heuristic_cost = heuristic(adjacent, end)
                total_cost = base_cost + rotation_penalty + heuristic_cost
                
                new_state = SearchState(
                    point=adjacent,
                    path=current_state.path + [adjacent],
                    direction=new_direction,
                    rotation_count=rotation_count,
                    total_cost=total_cost
                )
                
                heapq.heappush(open_set, new_state)
    
        return all_shortest_paths
    
    def get_all_paths(self, start: Point, end: Point, walls: list[Point], with_diagonals=False, max_paths=None, max_depth=None) -> list[list[Point]]:
        def dfs(current, path):
            if max_depth is not None and len(path) > max_depth:
                return
            if max_paths is not None and len(paths) >= max_paths:
                return
        
            if current == end:
                paths.append(path + [end])
                return
            
            visited.add(current)
            for adjacent in self.get_adjacent_positions(current, with_diagonals):
                if adjacent not in walls and adjacent not in visited:
                    dfs(adjacent, path + [adjacent])
            
            visited.remove(current)
        
        paths = []
        visited = set()
        dfs(start, [start])
        return paths
    
        
def get_groups(points: list[Point]) -> list[list[Point]]:
    groups = get_oriented_groups([(point, Point(0, 0)) for point in points])
    groups = [[point for point, _ in group] for group in groups]
    return groups

def get_oriented_groups(points: list[tuple[Point, Point]]) -> list[list[tuple[Point, Point]]]:
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

def merge_intervals(intervals: list[list]) -> list[list]:
    intervals.sort()
    stack = []
    stack.append(intervals[0])
    
    for interval in intervals[1:]:
        assert len(interval) == 2
        if stack[-1][0] <= interval[0] <= stack[-1][-1]:
            stack[-1][-1] = max(stack[-1][-1], interval[-1])
        else:
            stack.append(interval)
      
    return stack
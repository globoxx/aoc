import re

def extract_tuples(text: str):
    text = text.strip().replace("\n", " ")
    
    chars = list(text)
    print(chars)
    
    return chars

def search_word_in_grid(grid, word):
    rows = len(grid)
    cols = len(grid[0])

    def search_from_position(x, y, dx, dy):
        positions = []
        for i in range(len(word)):
            nx, ny = x + i * dx, y + i * dy
            if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == word[i]:
                positions.append((nx, ny))
            else:
                return None
        return positions

    directions = [
        (1, 1),
        (1, -1),
        (-1, -1),
        (-1, 1)
    ]

    all_occurrences = []

    for x in range(rows):
        for y in range(cols):
            for dx, dy in directions:
                result = search_from_position(x, y, dx, dy)
                if result:
                    all_occurrences.append(result)

    return all_occurrences

with open('2025/4/input.txt') as f:
    lines = f.readlines()
    grid = [extract_tuples(line) for line in lines]
    word = "MAS"
    all_positions = search_word_in_grid(grid, word)
    centers = []
    for positions in all_positions:
        center = positions[1]
        c = 0
        for p in all_positions:
            if p[1] == center:
                c += 1
        if c == 2 and center not in centers:
            centers.append(center)
        elif c > 2:
            print("Error")
    print(len(centers))

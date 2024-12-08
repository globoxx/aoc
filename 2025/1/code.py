import re

def extract_tuples(text: str):
    text = text.strip().replace("\n", " ")

    # Extract all numbers from the text
    numbers = re.findall(r"\d+", text)
    return tuple(map(int, numbers))

with open('2025/1/input.txt') as f:
    lines = f.readlines()
    numbers = [extract_tuples(line) for line in lines]
    col1 = [x[0] for x in numbers]
    col2 = [x[1] for x in numbers]
    col1_sorted = sorted(col1)
    col2_sorted = sorted(col2)
    distances = [abs(col1_sorted[i] - col2_sorted[i]) for i in range(len(col1_sorted))]
    total_distance = sum(distances)
    print(total_distance)

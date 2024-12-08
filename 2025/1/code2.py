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
    similarities = [col2.count(x)*x for x in col1]
    total_similarity = sum(similarities)
    print(total_similarity)

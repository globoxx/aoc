import re
import copy

def extract_tuples(text: str):
    text = text.strip().replace("\n", " ")

    # Extract all numbers from the text
    numbers = re.findall(r"\d+", text)
    return list(map(int, numbers))

def increasing(numbers: tuple):
    for i in range(len(numbers) - 1):
        if numbers[i] > numbers[i + 1]:
            return False
    return True

def decreasing(numbers: tuple):
    for i in range(len(numbers) - 1):
        if numbers[i] < numbers[i + 1]:
            return False
    return True

def differing(numbers: tuple):
    for i in range(len(numbers) - 1):
        if not (1 <= abs(numbers[i] - numbers[i + 1]) <= 3):
            return False
    return True

def is_safe(numbers: tuple):
    safe = (increasing(numbers) or decreasing(numbers)) and differing(numbers)
    if safe:
        return True
    for i in range(len(numbers)):
        numbers_bis = copy.deepcopy(numbers)
        del numbers_bis[i]
        safe = (increasing(numbers_bis) or decreasing(numbers_bis)) and differing(numbers_bis)
        if safe:
            return True
    return False

with open('2025/2/input.txt') as f:
    lines = f.readlines()
    numbers = [extract_tuples(line) for line in lines]
    safe = [is_safe(number) for number in numbers]
    total_safe = sum(safe)
    print(total_safe)

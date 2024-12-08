import re

def extract_tuples(text: str):
    pattern = r"mul\(\d+,\d+\)|do\(\)|don't\(\)"

    matches = re.findall(pattern, text)
    
    accepted_matches = []
    accepted = True
    for match in matches:
        print(match, accepted)
        if match == "do()":
            accepted = True
        elif match == "don't()":
            accepted = False
        else:
            if accepted:
                accepted_matches.append(match)
    
    numbers = [match[4:-1].split(",") for match in accepted_matches if match != "do()" and match != "don't()"]
    for pair in numbers:
        pair[0] = int(pair[0])
        pair[1] = int(pair[1])

    return numbers


with open('2025/3/input.txt') as f:
    lines = f.readlines()
    lines = "".join(lines)
    numbers = extract_tuples(lines)
    print(len(numbers))
    somme = 0
    print(numbers)
    for pair in numbers:
        somme += pair[0] * pair[1]
    print(somme)

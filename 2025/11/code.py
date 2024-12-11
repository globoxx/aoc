import path
import sys

directory = path.Path(__file__).absolute()
sys.path.append(directory.parent.parent)

from utils import Board, Point
from collections import Counter

# Partie 2 d'abord tentée en utilisant un cache pour les résultats intermédiaires dans une fonction récursive
# Abandon suite à trop d'erreurs à cause de la récursion
# Adoption de la méthode du Counter dont on m'a parlé, qui ne m'est pas venue intuitivement

def blink(counter):
    new_counter = Counter()
    
    for stone, count in counter.items():
        if stone == '0':
            new_counter['1'] += count
        elif len(stone) % 2 == 0:
            mid = len(stone) // 2
            left_stone = stone[:mid]
            right_stone = stone[mid:].lstrip('0') or '0'
            new_counter[left_stone] += count
            new_counter[right_stone] += count
        else:
            new_counter[str(int(stone) * 2024)] += count
                
    return new_counter

def all_blinks(stones, nb_blinks):
    counter = Counter(stones)
    
    for _ in range(nb_blinks):
        counter = blink(counter)
    
    return sum(counter.values())


with open('2025/11/input.txt') as f:
    lines = [line.strip() for line in f.read().strip().splitlines()]
    initial_stones = lines[0].split()
        
    print(all_blinks(initial_stones, 25))
    print(all_blinks(initial_stones, 75))
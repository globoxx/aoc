import path
import sys
import re
import numpy as np

directory = path.Path(__file__).absolute()
sys.path.append(directory.parent.parent)

from utils import Board, Point

def next_secret(secret):
    a = secret << 6
    secret = a ^ secret
    secret = secret % 16777216

    a = secret >> 5
    secret = a ^ secret
    secret = secret % 16777216

    a = secret << 11
    secret = a ^ secret
    secret = secret % 16777216

    return secret


with open('2025/22/input.txt') as f:
    lines = [line.strip() for line in f.read().strip().splitlines()]     
    
    secrets = list(map(int, lines))

    n = 2000
    data = {secret: {} for secret in secrets}
    for secret in secrets:
        init_secret = secret
        last_digits = [int(str(secret)[-1])]
        for i in range(n):
            secret = next_secret(secret)
            last_digits.append(int(str(secret)[-1]))
        changes = [last_digits[i+1] - last_digits[i] for i in range(len(last_digits)-1)]

        for i in range(3, len(changes)):
            price = last_digits[i+1]
            last_four_changes = tuple(changes[i-3:i+1])
            if last_four_changes not in data[init_secret]:
                data[init_secret][last_four_changes] = [price]
            else:
                data[init_secret][last_four_changes].append(price)

    all_last_four_changes = set()
    for secret in data:
        all_last_four_changes.update(data[secret].keys())

    print('Number of last four changes:', len(all_last_four_changes))

    best_profit = 0
    best_last_four_changes = None
    for last_four_changes in all_last_four_changes:
        profit = 0
        for secret in data:
            if last_four_changes in data[secret]:
                profit += data[secret][last_four_changes][0]
        if profit > best_profit:
            best_profit = profit
            best_last_four_changes = last_four_changes

    print(best_profit)
    print(best_last_four_changes)
    
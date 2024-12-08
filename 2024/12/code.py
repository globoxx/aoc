from functools import cache
from itertools import product
import re

# Input files not included in repo per copyright & Eric Wastl's request.
# https://www.reddit.com/r/adventofcode/wiki/faqs/copyright/inputs/
# Replace with path to your personal input file if you would like to run the code.
input_file = '12/input.txt'

# To match the format of input files for the Basilisk.
q = { 12: open(input_file).read().strip() }

######################### PART 1: MULTI-LINE SOLUTION #########################
springs = [x.split() for x in q[12].strip().split('\n')]
springs = [[x[0], [int(y) for y in x[1].split(',')]] for x in springs]

def count_permutations(symbols):
    results = set()

    for symbol, counts in symbols:
        possibilities = []
        for s in symbol:
            if s == '?':
                possibilities.append(['#', '.'])
            else:
                possibilities.append([s])

        for combo in product(*possibilities):
            candidate = ''.join(combo)
            matches = re.findall(r'#+', candidate)
            match_lengths = [len(x) for x in matches]
            if match_lengths == counts:
                results.add(candidate)

    return len(results)

counts = [count_permutations([s]) for s in springs]

print('Day 12 Part 1:',sum(counts))
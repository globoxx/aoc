import path
import sys

directory = path.Path(__file__).absolute()
sys.path.append(directory.parent.parent)

from utils import Board, Point

def get_last_occurence_index(lst, value):
    return max(index for index, item in enumerate(lst) if item == value)

def replace_x_last_occurences(lst, to_replace, new_value, x):
    count = 0
    for i in range(len(lst) - 1, -1, -1):
        if lst[i] == to_replace:
            lst[i] = new_value
            count += 1
            if count == x:
                break
    return lst

with open('2025/9/input.txt') as f:
    lines = [line.strip() for line in f.read().strip().splitlines()]
    line = list(lines[0])
    
    print(line)
    
    table = []
    x = 0
    for i, e in enumerate(line):
        if i % 2 == 0:
            to_add = [x]*int(e)
            x += 1
        else:
            to_add = ['.']*int(e)
        table.extend(to_add)
    print(table)

    reversed_table = [e for e in table[::-1] if e != '.']
    print(reversed_table)
    for i, bloc in enumerate(list(dict.fromkeys(reversed_table))):
        count = reversed_table.count(bloc)
        # print(bloc, count)
        for j, e in enumerate(table):
            if e == '.':
                free_space = 0
                k = j
                while table[k] == '.' and k < len(table) - 1:
                    k += 1
                    free_space += 1
                if free_space >= count:
                    table[j:j+count] = [bloc]*count
                    table = replace_x_last_occurences(table, bloc, '.', count)
                    break
    print(table)
    
    total = 0
    for i, e in enumerate(table):
        if e == '.':
            continue
        total += i*int(e)
        
    print(total)
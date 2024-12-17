import path
import sys
import re
import numpy as np

directory = path.Path(__file__).absolute()
sys.path.append(directory.parent.parent)

from utils import Board, Point

def get_candidates_example():
    # Designed to work with the example program, works
    k = 0
    while True:
        base = 8 * k
        
        for offset in range(8):
            a = base + offset
            # First constraint: (a // 2^3) mod 8 = 0
            first_div = (a // 8)
            if first_div % 8 == 0:
                # Second constraint: (((a // 2^3) // 2^3) mod 8 = 3
                second_div = (first_div // 8)
                if second_div % 8 == 3:
                    # Should continue with the rest of the constraints
                    yield a
        
        k += 1
        
def get_candidates(program):
    # Designed to work with the real program
    # Does not work, buggy and far too slow
    def make_computations(a, b, c):
        b = b % 8
        b = b ^ 1
        c = a // 2**b
        a = a // 8
        b = b ^ c
        a = a // 2**c
        return a, b, c
    
    k = 0
    while True:
        base = 8 * k
        b = 0
        c = 0
        
        for offset in range(8):
            a = base + offset
            a, b, c = make_computations(a, b, c)
            ok = True
            for output in program:
                if b != output:
                    ok = False
                    break
                a, b, c = make_computations(a, b, c)
            if ok:
                print(a)
                yield a
        k += 1            
    
def solve(program):
    sols = []
    stack = [(0, len(program) - 1)]
    while stack:
        current_a, current_pos = stack.pop()
        
        if current_pos < 0:
            sols.append(current_a)
            continue
        
        for offset in range(8):
            candidate_a = current_a * 8 + offset
            
            a = candidate_a
            b = 0
            c = 0
            output = None
            
            i = 0
            while i < len(program):
                opcode = program[i]
                operand = program[i + 1]
                
                combo = get_combo_operand(operand, a, b, c)
                
                if opcode == 0: 
                    a //= 2**combo
                elif opcode == 1: 
                    b ^= operand
                elif opcode == 2: 
                    b = combo % 8
                elif opcode == 3: 
                    if a != 0:
                        i = operand
                        continue
                elif opcode == 4: 
                    b ^= c
                elif opcode == 5: 
                    output = combo % 8
                    break
                elif opcode == 6: 
                    b = a // 2**combo
                elif opcode == 7: 
                    c = a // 2**combo
                
                i += 2
            
            if output == program[current_pos]:
                stack.append((candidate_a, current_pos - 1))
    
    return sols

def get_combo_operand(operand, a, b, c):
    return operand if operand < 4 else a if operand == 4 else b if operand == 5 else c

def run_program(registers, program, debug=False):
    i = 0
    outputs = []

    while i < len(program):
        opcode = program[i]
        operand = program[i + 1]
        
        a = registers['A']
        b = registers['B']
        c = registers['C']
        
        if debug:
            print(f'Registers state: {registers}')
            print(f'A value encoded:', bin(registers['A']))
            print(f'Instruction: {opcode} {operand}')

        if opcode == 0:
            divisor = 2 ** get_combo_operand(operand, a, b, c)
            registers['A'] = registers['A'] // divisor
        elif opcode == 1:
            registers['B'] ^= operand
        elif opcode == 2:
            registers['B'] = get_combo_operand(operand, a, b, c) % 8
        elif opcode == 3:
            if registers['A'] != 0:
                i = operand
                continue 
        elif opcode == 4:  
            registers['B'] ^= registers['C']
        elif opcode == 5:
            outputs.append(get_combo_operand(operand, a, b, c) % 8)
        elif opcode == 6:
            divisor = 2 ** get_combo_operand(operand, a, b, c)
            registers['B'] = registers['A'] // divisor
        elif opcode == 7:
            divisor = 2 ** get_combo_operand(operand, a, b, c)
            registers['C'] = registers['A'] // divisor

        i += 2

    return outputs

with open('2025/17/input.txt') as f:
    lines = [line.strip() for line in f.read().strip().splitlines()]     
    
    registers = {}
    registers['A'] = int(lines[0].split(':')[1].strip())
    registers['B'] = int(lines[1].split(':')[1].strip())
    registers['C'] = int(lines[2].split(':')[1].strip())
    
    program = lines[4].split(':')[1].strip().split(',')
    program_str = ','.join(program)
    program = list(map(int, program))
    print(registers)
    print(program)
    
    outputs = run_program(registers, program, debug=True)
    
    sols = solve(program)
    print(sols)
    print(min(sols))
    
    '''
    candidates = get_candidates(program)
    for k, v in enumerate(candidates):
        registers['A'] = v
        outputs = run_program(registers, program)
        outputs = ','.join(map(str, outputs))
        if outputs == program_str:
            print(v)
            break
        k += 1
    '''
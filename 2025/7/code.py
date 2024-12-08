import re
from itertools import product

def extract_tuples(text: str):
    text = text.strip().replace("\n", " ")

    numbers = re.findall(r"\d+", text)
    return list(map(int, numbers))

def calcul_gauche_droite(nombres, ops):
    resultat = nombres[0]
    for i in range(len(ops)):
        if ops[i] == '+':
            resultat += nombres[i+1]
        elif ops[i] == "||":
            resultat = int(str(resultat) + str(nombres[i+1]))
        else:
            resultat *= nombres[i+1]
    return resultat

with open('2025/7/input.txt') as f:
    lines = f.readlines()
    numbers = [extract_tuples(line) for line in lines]
    
    total = 0
    for line in numbers:
        result = line[0]
        rest = line[1:]
        ops = list(product(['+', '*', "||"], repeat=(len(rest) - 1)))
        n = 0
        # print(ops)
        for op in ops:
            calcul = ""
            for i in range(len(rest) - 1):
                calcul += str(rest[i]) + op[i]
            calcul += str(rest[-1])
            if calcul_gauche_droite(rest, op) == result:
                # print(str(result) + "=" + calcul)
                n += result
                break
            else:
                # print(calcul + "!=" + str(result))
                pass
        
        total += n
    print(total)


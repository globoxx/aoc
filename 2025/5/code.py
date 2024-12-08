import re
from collections import defaultdict, deque

def extract_tuples(text: str):
    text = text.strip().replace("\n", " ")

    numbers = re.findall(r"\d+", text)
    return list(map(int, numbers))

def reorder_list(nombres, contraintes):
    contraintes = [(x, y) for (x, y) in contraintes if x in nombres and y in nombres]
    
    graphe = {n: [] for n in nombres}
    deg = {n: 0 for n in nombres}
    
    for x, y in contraintes:
        graphe[x].append(y)
        deg[y] += 1
    
    queue = deque([n for n in nombres if deg[n] == 0])

    resultat = []
    while queue:
        actuel = queue.popleft()
        resultat.append(actuel)
        
        for v in graphe[actuel]:
            deg[v] -= 1
            if deg[v] == 0:
                queue.append(v)
    
    restants = set(nombres) - set(resultat)
    resultat.extend(restants)
    
    return resultat

rules = None
with open('2025/5/input.txt') as f:
    lines = f.readlines()
    rules = [extract_tuples(line) for line in lines]    
    
with open('2025/5/updates.txt') as f:
    lines = f.readlines()
    updates = [extract_tuples(line) for line in lines]
    
    somme = 0
    for update in updates:
        update = list(update)
        ok = True
        for rule in rules:
            before = rule[0]
            after = rule[1]
            if before in update and after in update and update.index(before) > update.index(after):
                ok = False
                break
        if not ok:
            update_corrected = reorder_list(update, rules)
            somme += update_corrected[len(update_corrected)//2]

    print(somme)
            
    

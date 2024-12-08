with open('4/input.txt') as f:
    lines = f.readlines()
    copies = [1 for _ in range(len(lines))]
    for i, line in enumerate(lines):
        cards = line.split(':')[-1]
        winner_cards, owned_cards = cards.split('|')
        winner_cards = set(winner_cards.split())
        owned_cards = set(owned_cards.split())
        count = 0
        for owned_card in owned_cards:
            if owned_card in winner_cards:
                count += 1
        for j in range(i+1, i+1+count):
            copies[j] += copies[i]
    total = sum(copies)
    print(total)
        
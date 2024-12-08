with open('4/input.txt') as f:
    lines = f.readlines()
    total_gain = 0
    for line in lines:
        cards = line.split(':')[-1]
        winner_cards, owned_cards = cards.split('|')
        winner_cards = set(winner_cards.split())
        owned_cards = set(owned_cards.split())
        gain = 0
        for owned_card in owned_cards:
            if owned_card in winner_cards:
                if gain == 0:
                    gain = 1
                else:
                    gain *= 2
        total_gain += gain
    print(total_gain)
from collections import Counter
import functools


def get_type(hand):
    highest = 0
    for p in ['A', 'K', 'Q', 'T'] + [str(x) for x in list(range(2, 10))]:
        hand_bis = hand.replace('J', p)
        counter = Counter(hand_bis)
        v = 0
        if len(set(hand_bis)) == 1:
            v = 7
        elif counter.most_common(1)[0][1] == 4:
            v = 6
        elif counter.most_common(2)[0][1] == 3 and counter.most_common(2)[1][1] == 2:
            v = 5
        elif counter.most_common(2)[0][1] == 3:
            v = 4
        elif counter.most_common(2)[0][1] == 2 and counter.most_common(2)[1][1] == 2:
            v = 3
        elif counter.most_common(2)[0][1] == 2:
            v = 2
        else:
            v = 1
        if v > highest:
            highest = v
    return highest
    
def try_conversion(c):
    data = {
        'A': 14,
        'K': 13,
        'Q': 12,
        'J': 1,
        'T': 10
    }
    if c in data:
        return data[c]
    else:
        return int(c)
    
def compare(h1, h2):
    t1 = get_type(h1)
    t2 = get_type(h2)
    if t1 < t2:
        return -1
    elif t2 < t1:
        return 1
    else:
        for c1, c2 in zip(h1, h2):
            c1 = try_conversion(c1)
            c2 = try_conversion(c2)
            if c1 < c2:
                return -1
            elif c2 < c1:
                return 1
    return 0


with open('7/input.txt') as f:
    lines = [line.strip() for line in f.readlines()]
    hands = [line.split()[0] for line in lines]
    bids = [line.split()[1] for line in lines]
    hand_to_bid = {hand: int(bid) for hand, bid in zip(hands, bids)}

    hands = sorted(hands, key=functools.cmp_to_key(compare))
    total = 0
    for i, hand in enumerate(hands):
        rank = i+1
        bid = hand_to_bid[hand]
        #print(hand, rank, bid)
        total += bid*rank
    
    print(total)
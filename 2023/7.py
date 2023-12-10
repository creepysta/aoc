from collections import defaultdict
from utils import lines as flines


def parser(fpath: str):
    lines = flines(fpath)
    return list(map(lambda x: (x.split(' ')[0], int(x.split(' ')[1])), lines))


types = {5: 999, 41: 888, 32: 777,  311: 666, 221: 555, 2111: 444, 11111: 333}
cards = [ 'A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2' ][::-1]
cards_j = [ 'A', 'K', 'Q', 'T', '9', '8', '7', '6', '5', '4', '3', '2', 'J'][::-1]


def max_key(d: dict):
    return max(map(lambda x: (x[1], x[0]), d.items()))[1]


def classify(hand, bid, joker=False):
    curr = defaultdict(int)

    for ch in hand:
        curr[ch] += 1

    if joker and len(curr) > 1:
        cnt = curr.pop('J', 0)
        curr[max_key(curr)] += cnt


    match len(curr.keys()):
        case 1: # 5
            return (types[5], hand, bid)
        case 2: # 4 or full house
            if min(curr.values()) == 1:
                return (types[41], hand, bid)
            else:
                return (types[32], hand, bid)
        case 3: # 3 or 2 pair
            if max(curr.values()) == 3:
                return (types[311], hand, bid)
            else:
                return (types[221], hand, bid)
        case 4: # one pair
            return (types[2111], hand, bid)
        case 5: # high card
            return (types[11111], hand, bid)


def card_comp(hand: str, joker):
    col = cards if not joker else cards_j
    got = tuple(col.index(x) for x in hand)
    return got

def sort(val: tuple[int, str, int], joker=False):

    return (val[0], card_comp(val[1], joker))

def one():
    parsed = parser("7.in1")
    rv = []
    for hand, bid in parsed:
        rv.append(classify(hand, bid))

    rv.sort(key=sort)

    ans = 0
    for i, e in enumerate(rv, start=1):
        ans += i * e[2]

    print("ONE:", ans)

def two():
    parsed = parser("7.in1")
    rv = []
    for hand, bid in parsed:
        rv.append(classify(hand, bid, True))

    rv.sort(key=lambda x: sort(x, joker=True))

    ans = 0
    for i, e in enumerate(rv, start=1):
        ans += i * e[2]
    print("TWO:", ans)


one()
two()

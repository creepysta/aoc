from utils import lines as flines, bench


class Card:
    def __init__(self, win, mine, card_id):
        self.win = win
        self.mine = mine
        self.card_id = card_id


def parser(fpath: str) -> dict[int, Card]:
    lines = flines(fpath)
    rv = {}
    for line in lines:
        card, numbers = line.split(':')
        card_id = int(card.split()[-1].strip())
        win, my = numbers.split('|')
        rwin = [int(x.strip()) for x in win.split()]
        rmy = [int(x.strip()) for x in my.split()]
        rv[card_id] = Card(rwin, rmy, card_id)

    return rv


def one():
    parsed = parser("4.in1")
    ans = 0
    for e in parsed.values():
        comm = len(set(e.win).intersection(e.mine))
        if comm:
            ans += pow(2, comm-1)

    print("ONE:", ans)

@bench
def two():
    parsed = parser("4.in1")
    maxid = max(parsed.keys())
    rv = [x for x in parsed.values()]
    for card in rv:
        curr_id = card.card_id
        comm = len(set(card.win).intersection(card.mine))
        for cid in range(curr_id+1, min(curr_id + comm, maxid)+1):
            rv.append(parsed[cid])

    print("TWO:", len(rv))


one()
two()

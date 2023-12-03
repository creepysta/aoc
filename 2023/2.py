from functools import reduce
from pprint import pprint
from utils import lines as flines


given = {
    'red': 12,
    'green': 13,
    'blue': 14,
}

def parser(fpath: str) -> dict:
    lines = flines(fpath)
    games = {}
    for line in lines:
        game, game_str = line.split(':')
        game_id = int(game.strip().split(' ')[1])
        games[game_id] = []
        parts = game_str.strip().split(';')
        for part in parts:
            data = {}
            for q in part.split(','):
                qnt, color = q.strip().split(' ')
                data[color] = int(qnt)
            games[game_id].append(data)

    return games


def one():
    def possible(data: list):
        for val in data:
            for k, v in given.items():
                if val.get(k, 0) > v:
                    return False

        return True

    games = parser("2.in1")
    ans = 0
    for gid, data in games.items():
        if possible(data):
            ans += gid

    print("ONE:", ans)

def two():
    def possible(data: list):
        maybe = {k: -1 for k in given}
        for val in data:
            for k in maybe:
                maybe[k] = max(maybe[k], val.get(k, 0))

        return maybe

    games = parser("2.in1")
    ans = 0
    for _, data in games.items():
        got = possible(data)
        cal = reduce(lambda x, y: x*y, got.values(), 1)
        ans += cal

    print("TWO:", ans)


one()
two()

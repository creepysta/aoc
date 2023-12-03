from functools import reduce, partial
from utils import lines as flines
from pprint import pprint


def parser(fpath: str):
    lines = flines(fpath)
    m = [[ch for ch in x] for x in lines]
    return m


def is_digit(ch: str):
    return ch.isdigit()


def is_dot(ch: str):
    return ch == '.'


def is_symbol(ch):
    return not (is_digit(ch) or is_dot(ch))

def is_valid(p: tuple, dim: tuple):
    return 0 <= p[0] < dim[0] and 0 <= p[1] < dim[1]

def dir_tuples(pos: tuple[int, int], dim: tuple[int, int], group_row=False) -> list[tuple[int, int]]:
    def np(a: tuple[int, int], b: tuple[int, int]) -> tuple[int, int] | None:
        p = (a[0] + b[0], a[1] + b[1])
        if is_valid(p, dim):
            return p

        return None

    ps = [-1, 0, 1]
    dirs: list
    if group_row:
        dirs = [[np((y, x), pos) for x in ps if np((y, x), pos)] for y in ps]
    else:
        dirs = [np((y, x), pos) for y in ps for x in ps if np((y, x), pos)]
    return dirs  # type: ignore


def process(point: tuple[int, int], g: list[list[str]], dims: tuple[int, int], vis: list[list[bool]]) -> int | None:
    y, x = point
    if not is_digit(g[y][x]) or vis[y][x]:
        return None

    while is_valid((y, x), dims) and is_digit(g[y][x]):
        x -= 1

    x += 1
    ch = ''
    while is_valid((y, x), dims) and is_digit(g[y][x]):
        ch += g[y][x]
        vis[y][x] = True
        x += 1

    return int(ch)


def one():
    parsed = parser("3.in1")
    symbols_pos = [
        (i, j)
        for i, row in enumerate(parsed)
        for j, ch in enumerate(row) if is_symbol(ch)
    ]
    dims = len(parsed), len(parsed[0])
    vis = [[False for _ in range(dims[1])] for _ in range(dims[0])]
    start_vs = [dir_tuples(pos, dims) for pos in symbols_pos]
    calc = partial(process, vis=vis, g=parsed, dims=dims)

    ans = 0
    for maybe in start_vs:
        for point in maybe:
            val = calc(point)
            if val is not None:
                ans += val

    print("ONE:", ans)

def two():
    parsed = parser("3.in1")
    symbols_pos = [
        (i, j)
        for i, row in enumerate(parsed)
        for j, ch in enumerate(row) if ch == '*'  # gear symbol
    ]
    dims = len(parsed), len(parsed[0])
    vis = [[False for _ in range(dims[1])] for _ in range(dims[0])]
    calc = partial(process, vis=vis, g=parsed, dims=dims)

    ans = 0
    for spos in symbols_pos:
        vals = []
        for point in dir_tuples(spos, dims, False):
            got = calc(point)
            if got is not None:
                vals.append(got)

        if len(vals) > 1:
            ans += reduce(lambda x, y: x * y, vals, 1)

    print("TWO:", ans)


one()
two()

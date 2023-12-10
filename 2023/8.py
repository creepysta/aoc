from math import lcm
from functools import reduce
from collections import defaultdict
from utils import lines as flines
from pprint import pprint


def parser(fpath: str):
    lines = flines(fpath)
    dirs = lines[0]
    g = {}
    for line in lines[2:]:
        start, rest = line.split('=')
        points = list(map(lambda x: x.strip(' ()'), rest.split(',')))
        g[start.strip()] = tuple(points)

    return dirs, g


dirc = {'L': 0, 'R': 1}


def one():
    dirs, g = parser("8.in2")
    u = 'AAA'
    ans = 0
    dirpos = 0
    while True:
        ch = dirs[dirpos]
        v = g[u][dirc[ch]]
        ans += 1
        if v == 'ZZZ':
            break

        u = v
        dirpos = (dirpos + 1) % len(dirs)

    print("ONE:", ans)


def two():
    dirs, g = parser("8.in3")
    starts = [x for x in g if x.endswith('A')]

    ans = 0
    dirpos = 0
    def is_end():
        for start in starts:
            if not start.endswith('Z'):
                return False

        return True

    while True:
        ch = dirs[dirpos]
        for vpos, _ in enumerate(starts):
            starts[vpos] = g[starts[vpos]][dirc[ch]]

        ans += 1
        dirpos = (dirpos + 1) % len(dirs)
        if is_end():
            break

    print("TWO:", ans)


def two_2():
    dirs, g = parser("8.in2")
    starts = [x for x in g if x.endswith('A')]
    _starts = starts[:]

    freq = {x: [] for x in _starts}
    # freq = {x: 0 for x in _starts}
    for start in starts:
        u = start
        cnt = 0
        dirpos = 0
        pathlen = 0
        while True:
            ch = dirs[dirpos]
            v = g[u][dirc[ch]]
            pathlen += 1
            if v[-1] == 'Z':
                # freq[start] = pathlen
                # break
                cnt += 1
                if cnt == 2:
                    freq[start].append(pathlen)
                    break

                freq[start].append(pathlen)
                pathlen = 0

            u = v
            dirpos = (dirpos + 1) % len(dirs)

    print("LCM:", lcm(*[x[0] for x in  freq.values()]))
    # print("LCM:", lcm(*[x for x in  freq.values()]))


one()
two()
two_2()


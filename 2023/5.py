from utils import lines as flines

class Range:
    def __init__(self, src: str, dst: str, rng: str):
        self.src = int(src)
        self.dst = int(dst)
        self.rng = int(rng)

class Maps:
    def __init__(self, ranges: list[Range]):
        self.ranges = ranges

    def get(self, x: int) -> int:
        for r in self.ranges:
            # eg; dst - 90, range - 2 -> vals: 90, 91
            if r.src <= x < r.src + r.rng:
                return r.dst + (x - r.src)

        # if there are no ranges, consider the key itself
        return x

    def sat_range(self, start: int, end: int) -> list[tuple[int, int]]:



        return rv


class Inp:
    def __init__(self, seeds: str, maps: dict[str, Maps]):
        self.seeds = self.parse_seeds(seeds)
        self.maps = maps

    def parse_seeds(self, seeds: str) -> list[int]:
        right = seeds.split(':')[1]
        return [int(x.strip()) for x in right.split()]


def parser(fpath: str):
    lines = (x for x in flines(fpath))
    seeds = next(lines)
    next(lines)
    maps: dict[str, Maps] = {}
    for line in lines:
        name = line.split(' ')[0].strip()
        ranges: list[Range] = []
        for l in lines:
            if not l:
                break

            dst, src, rng = l.split(' ')
            ranges.append(Range(src, dst, rng))

        maps[name] = Maps(ranges)

    inp = Inp(seeds, maps)
    return inp


def one():
    inp = parser("5.in1")
    seeds = inp.seeds
    maps = inp.maps
    maybe = {x: x for x in seeds}
    order = maps.keys()
    for o in order:
        curr = maps[o]
        for seed in seeds:
            maybe[seed] = curr.get(maybe[seed])


    ans = min(maybe.values())
    print("ONE:", ans)


def smaller_intervals(low, high):
    m = int(1e7)
    print(f"{low=}, {high=}")
    steps = (high-low + m-1)// m
    for i, rlow in enumerate(range(low, high, m)):
        print(f"Running: {i}/{steps}...")
        yield rlow, min(high, rlow + m)


# stupid
def two():
    inp = parser("5.in1")
    seeds = inp.seeds
    maps = inp.maps
    order = maps.keys()
    col = []
    for s_start, s_rng in zip(seeds[0::2], seeds[1::2]):
        low, high = s_start, s_start + s_rng
        intv_col = []
        for intv_s, intv_e in smaller_intervals(low, high):
            seeds = list(range(intv_s, intv_e))
            maybe = {x: x for x in seeds}
            for _, o in enumerate(order):
                curr = maps[o]
                for seed in seeds:
                    maybe[seed] = curr.get(maybe[seed])

            intv_col.append(min(maybe.values()))

        col.append(min(intv_col))

    ans = min(col)
    print("TWO:", ans)


def two_2():
    inp = parser("5.in")
    inp_seeds = inp.seeds
    seeds = [(s, s+r) for s, r in zip(inp_seeds[0::2], inp_seeds[1::2])]
    maps = inp.maps
    order = maps.keys()
    col = []
    # work with ranges instead of single seed
    for s_start, s_end in seeds:
        intv_col = []
        for o in order:
            curr = maps[o]
            # curr.sat_range(s_start, s_end)

    ans = min(col)
    print("TWO:", ans)

one()
if 1 == 2: two()
else: two_2()
